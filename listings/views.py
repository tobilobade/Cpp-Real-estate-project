from django.shortcuts import render, redirect, get_object_or_404
from .models import House  # Import the House model
from .forms import HouseForm
import boto3

# Create your views here.
# def homepage(request):
#     return render(request, 'listings/property_homepage.html')
def homepage(request):
    featured_properties = House.objects.all()[:5]  # Fetch the first 5 properties for the homepage
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
    
def delete_house(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        house.delete()
        return redirect('sell_house')  # Redirect to homepage after successful deletion
    return render(request, 'listings/sell_house.html', {'house_to_delete': house})