from django.shortcuts import render, redirect, get_object_or_404
import boto3
from .models import House  # Import the House model
from .forms import HouseForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
# def homepage(request):
#     return render(request, 'listings/property_homepage.html')
def homepage(request):
    featured_properties = House.objects.all()[:6]
    return render(request, 'listings/property_homepage.html', {'properties': featured_properties})

def sell_house(request):
    houses = House.objects.all() 
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
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
    # Retrieve all properties
    all_properties = House.objects.all()
    return render(request, 'listings/more_properties.html', {'properties': all_properties})

def property_detail(request, house_id):
    # Fetch the house object corresponding to the house_id
    house = get_object_or_404(House, pk=house_id)
    return render(request, 'listings/property_detail.html', {'property': house})
    
def delete_house(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        house.delete()
        return redirect('sell_house')  # Redirect to homepage after successful deletion
    return render(request, 'listings/sell_house.html', {'house_to_delete': house})
    
# def subscribe_to_newsletter(request):
#     if request.method == 'POST':
#         # Get email address from the form
#         email = request.POST.get('email')
        
#         # Subscribe the user to the SNS topic
#         sns_client = boto3.client('sns', region_name='eu-west-1')
#         topic_arn = 'arn:aws:sns:eu-west-1:250738637992:x23212365-Real-estate'
#         subscription = sns_client.subscribe(
#             TopicArn=topic_arn,
#             Protocol='email',
#             Endpoint=email
#         )
        
#         # Send confirmation message
#         if subscription['ResponseMetadata']['HTTPStatusCode'] == 200:
#             message = """
#             Hi there,

#             Thank you for subscribing to our newsletter! You'll now receive the latest updates and news about our real estate listings.

#             Best regards,
#             The Modak Estate Team
#             """            
#             sns_client.publish(
#                 TopicArn=topic_arn,
#                 Message=message,
#                 Subject='Newsletter Subscription Confirmation'
#             )
#             return render(request, 'listings/subscription_success.html')
#         else:
#             # Handle subscription failure
#             return render(request, 'listings/subscription_failure.html')
#     else:
#         # Handle GET request (render homepage with subscription form)
#         return render(request, 'listings/property_homepage.html')

def subscribe_to_newsletter(request):
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
            sender=f'{sender_name} <{settings.DEFAULT_FROM_EMAIL}>',  # Combine sender's name with default email address
            recipient_list=[email],
            fail_silently=False,
            html_message=message
        )

        # Subscribe the user to the SNS topic
        sns_client = boto3.client('sns', region_name='eu-west-1')
        topic_arn = 'arn:aws:sns:eu-west-1:250738637992:x23212365-Real-estate'
        sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
        )

        return render(request, 'listings/subscription_success.html')
    else:
        # Handle GET request (render homepage with subscription form)
        return render(request, 'listings/property_homepage.html')
