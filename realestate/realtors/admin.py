from django.contrib import admin
from realtors.models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    class Meta:
        model = Realtor

    list_display = ['id', 'name', 'email', 'phone', 'is_mvp', ]
    list_display_links = ['id', 'name', ]
    list_filter = ('name',)
    list_editable = ('phone', 'is_mvp',)
    search_fields = ('name', 'email',)
    list_per_page = 3


# Register your models here.
admin.site.register(Realtor, RealtorAdmin)