""" file for the view functions"""
import boto3
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseForbidden,JsonResponse
from django_countries import countries
from ip_location_pkg.findAddress import get_ip_location
from .house_search import search_houses
from .models import House  # Import the House model
from .forms import HouseForm


def get_ip_location_view():
    """View function for the ip library."""
    # Call the function to get IP location
    ip_location = get_ip_location()
    if ip_location:
        # If IP location is retrieved successfully, return it as JSON response
        return JsonResponse(ip_location)
    return JsonResponse({'error': 'Failed to retrieve IP location.'}, status=500)

def homepage(request):
    """View function for the homepage."""
    featured_properties = House.objects.all()[:6]
    return render(request, 'listings/property_homepage.html', {'properties': featured_properties, 'user': request.user})

@login_required
def sell_house(request):
    """View function for the selling properties."""
    houses = House.objects.all()
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.user = request.user
            house.save()  # Saved the house object to generate a primary key
            # Uploaded the file to S3
            s3 = boto3.client('s3')
            bucket_name = 'x23212365-my-newtest-bucket'
            object_name = f'{house.image.name}'
            s3.upload_fileobj(house.image, bucket_name, object_name)
            # Updated the house object with the S3 URL
            house.image_url = f'https://{bucket_name}.s3.amazonaws.com/{object_name}'
            house.save()

            return redirect('homepage')  # Redirect to homepage after successful submission
    else:
        form = HouseForm()
    houses = House.objects.filter(user=request.user)
    return render(request, 'listings/sell_house.html', {'form': form ,'houses': houses})

def render_buy_houses(request):
    """
    Render a list of houses available for sale.
    """
    buy_houses = House.objects.filter(status='sale')
    return render(request, 'listings/buy_houses.html', {'buy_houses': buy_houses})

def render_rent_houses(request):
    """
    Render a list of houses available for rent.
    """
    rent_houses = House.objects.filter(status='rent')
    return render(request, 'listings/rent_houses.html', {'rent_houses': rent_houses})

def view_more_properties(request):
    """View function for the viewing more properties."""
    # Retrieve all properties
    all_properties = House.objects.all()
    return render(request, 'listings/more_properties.html', {'properties': all_properties})

def property_detail(request, house_id):
    """View function for getting the propety detail."""
    # Fetch the house object corresponding to the house_id
    house = get_object_or_404(House, pk=house_id)
    return render(request, 'listings/property_detail.html', {'property': house})


@login_required
def delete_house(request, house_id):
    """View function for the deleting houses."""
    user = request.user
    house = get_object_or_404(House, pk=house_id)
    if house.user == request.user:
        if request.method == 'POST':
            house.delete()
            return redirect('sell_house')  # Redirect to homepage after successful deletion
        return render(request, 'listings/sell_house.html', {'house_to_delete': house})
    else:
        return HttpResponseForbidden("You are not authorized to delete this house.")

def update_house(request, house_id):
    """View function for updating listings."""
    # Get the house object
    house = get_object_or_404(House, pk=house_id)

    if request.method == 'POST':
        # Create a form instance with the POST data and the instance of the house object
        form = HouseForm(request.POST, request.FILES, instance=house)

        if form.is_valid():
            # Save the form to update the house details
            form.save()
            return redirect('homepage')  # Redirect to homepage after successful update

    else:
        # If it's a GET request, create a form instance with the instance of the house object
        form = HouseForm(instance=house)

    return render(request, 'listings/update_house.html', {'form': form})


def subscribe_to_newsletter(request):
    """View function for subscribing to news letter."""
    if request.method == 'POST':
        # Get email address from the form
        email = request.POST.get('email')

        # Custom message for the subscription confirmation email
        custom_message = "Thank you for subscribing to our newsletter! We're excited to keep you updated with the latest news and updates."

        # Send subscription confirmation email using Django's email functionality
        subject = 'Newsletter Subscription Confirmation'
        message = custom_message  # Use your custom message here
        sender_name = 'Modak'  # Specify the sender's name
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # Combine sender's name with default email address
            [email],
            fail_silently=False,
            html_message=message
        )

        # # Subscribe the user to the SNS topic
        # sns_client = boto3.client('sns', region_name='eu-west-1')
        # topic_arn = 'arn:aws:sns:eu-west-1:250738637992:x23212365-Real-estate'
        # sns_client.subscribe(
        #     TopicArn=topic_arn,
        #     Protocol='email',
        #     Endpoint=email
        # )

        return render(request, 'listings/subscription_success.html')
    else:
        # Handle GET request (render homepage with subscription form)
        return render(request, 'listings/property_homepage.html')


def search_view(request):
    """View function for the search functionality."""
    if request.method == 'POST':
        # Extract search criteria from form data
        country_name = request.POST.get('country')
        status = request.POST.get('status')

        # Convert country name to country code
        country_code = get_country_code(country_name)

        # Perform search using library function
        houses = search_houses(country_code, status)

        # Pass search results to template for rendering
        return render(request, 'listings/search_result.html', {'houses': houses})
    else:
        # Render the search form
        return render(request, 'search_form.html')

def get_country_code(country_name):
    """View function for the country code converter."""
    try:
        country_code = [code for code, name in countries if name == country_name][0]
        return country_code
    except IndexError:
        return None


def about_us(request):
    """View function for the about page."""
    return render(request, 'listings/about.html')


def contact_us(request):
    """View function for the contact page."""
    return render(request, 'listings/contact_us.html')
    