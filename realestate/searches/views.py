from django.shortcuts import render
from searches.model_choices import state_choice, price_choice, Bedrooms_choice
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.
def search(request):
    method_dict = request.GET.copy()
    keywords = method_dict.get('keywords') or None
    city = method_dict.get('city') or None
    listing_ = Listing.objects.filter(is_published=True).all()

    # keywords
    if keywords is not None:
        keywords = method_dict.get('keywords')
        listing_ = listing_.filter(description__icontains=keywords)
    # city
    if city is not None:
        city = method_dict.get('city')
        listing_ = listing_.filter(city__icontains=city)

    # state
    if 'state' in method_dict:
        state = method_dict.get('state')
        listing_ = listing_.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in method_dict:
        bedrooms = method_dict.get('bedrooms')
        listing_ = listing_.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in method_dict:
        price = method_dict.get('price')
        listing_ = listing_.filter(price__lte=price)

    context = {
        'state_choice': state_choice,
        'price_choice': price_choice,
        'Bedrooms_choice': Bedrooms_choice,
        'method_dict': method_dict,
        'Listing_': listing_,
    }
    return render(request, 'searches/search.html',context)
