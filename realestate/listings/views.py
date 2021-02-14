from django.contrib import messages
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
# from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import Listing, Inquiry


# Create your views here.
def listings(request):
    listings_ = Listing.objects.all()
    paginator = Paginator(listings_, 3)
    page = request.GET.get("page", 1)
    try:
        listing_1 = paginator.page(page)
    except PageNotAnInteger:
        listing_1 = paginator.page(1)
    except EmptyPage:
        listing_1 = paginator.page(paginator.num_pages)
    # print(listing_1)
    context = {
        "listings_": listings_,
        "listings_": listing_1,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_id = Listing.objects.get(id=listing_id)
    context = {
        "Listing_": listing_id,
    }
    return render(request, 'listings/listing.html', context)


def listing_inquiry(request):
    if request.method == "POST":
        get_method = request.POST.copy()
        listing_IN = get_method.get('listing')
        print(listing_IN)
        phone = get_method.get('phone')
        print(phone)
        message = get_method.get('message')
        print(message)

        listing_object = Listing.objects.get(title=listing_IN)
        inquiry_exist = Inquiry.objects.filter(listing=listing_object, user=request.user)

        # print(listing_object)
        if not inquiry_exist:
            Inquiry.objects.create(listing=listing_object, user=request.user, phone=phone, message=message)
            send_mail(
                'Inquiry listing from DJRS',
                'Thank you for contacting us. We will contact you soon',
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, 'Inquiry message sent successfully')

        else:
            messages.error(request, 'Log In first')

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
