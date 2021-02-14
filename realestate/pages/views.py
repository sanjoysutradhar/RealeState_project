from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from searches.model_choices import price_choice,state_choice,Bedrooms_choice


# Create your views here.
def home(request):
    latest_list=Listing.objects.order_by('-list_date')[:3]
    context={
        'state_choice': state_choice,
        'Bedrooms_choice': Bedrooms_choice,
        'price_choice': price_choice,
        "latest_list":latest_list,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    list_realtor= Realtor.objects.order_by('-contact_date')[:3]
    seller_of_month = Realtor.objects.filter(is_mvp=True).first()
    context={
        "list_realtor": list_realtor,
        "seller_of_month": seller_of_month,
    }
    return render(request, 'pages/about.html', context)
