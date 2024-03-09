from .models import House

def search_houses(country, status):
    """
    Search for houses based on the country and status.

    Args:
        country (str): The country name.
        status (str): The status of the house (e.g., 'rent' or 'sale').

    Returns:
        QuerySet: A queryset containing the matching house listings.
    """
    # Filter houses based on the country and status
    houses = House.objects.filter(country=country, status=status)
    return houses
