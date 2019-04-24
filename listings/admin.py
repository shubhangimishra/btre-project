from django.contrib import admin
from .models import Listing
# Register your models here.
#admin.site.register(Listing)
 
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title') #it creates hyperllink
    list_filter = ('realtor',) # display side filtering
    list_editable = ('is_published',) # editable which we can edit (tick we can remove)
    search_fields = ('title','description','address','city','state','zipcode','price') #seach
    list_per_page = 25
admin.site.register(Listing,ListingAdmin)