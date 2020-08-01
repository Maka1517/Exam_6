from django.contrib import admin
from .models import Guest

class GuestAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('pk','name','email','updated_at','status')
    list_display_links = ('pk', 'name')
    search_fields = ('name',)

admin.site.register(Guest,GuestAdmin)

