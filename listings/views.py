from django.shortcuts import render, redirect, get_object_or_404
from .models import House  # Import the House model
from .forms import HouseForm

# Create your views here.
# def homepage(request):
#     return render(request, 'listings/property_homepage.html')
def homepage(request):
    featured_properties = House.objects.all()[:5]  # Fetch the first 5 properties for the homepage
    return render(request, 'listings/property_homepage.html', {'properties': featured_properties})

def sell_house(request):
    houses = House.objects.all()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to homepage after successful submission
    else:
        form = HouseForm()
    return render(request, 'listings/sell_house.html', {'form': form, 'houses': houses})
    
def delete_house(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        house.delete()
        return redirect('sell_house')  # Redirect to homepage after successful deletion
    return render(request, 'listings/sell_house.html', {'house_to_delete': house})