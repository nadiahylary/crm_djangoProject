from django.contrib import admin

from crm.models import Customer


class CustomAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')


# Register your models here.
admin.site.register(Customer, CustomAdmin)
