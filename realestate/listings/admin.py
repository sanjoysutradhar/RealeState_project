from django.contrib import admin
from listings.models import Listing, Inquiry


class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing

    list_display = ['id', 'realtor', 'title', 'address', 'price', 'is_published', 'city', 'state', 'bedrooms',
                    'description']
    list_display_links = ['id', 'realtor', ]
    list_filter = ('realtor',)
    list_editable = ('is_published', 'title', 'price', 'city', 'state', 'bedrooms', 'description', 'title',)
    search_fields = ('id', 'realtor', 'title', 'address', 'price',)
    list_per_page = 2


# Register your models here.
admin.site.register(Listing, ListingAdmin)


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['listing', 'user', 'phone', ]

    class Meta:
        model = Inquiry


# Register your models here.
admin.site.register(Inquiry, InquiryAdmin)
