from django.contrib import admin
from .models import CabsOnlineForm ,Trips

# Register your models here.
@admin.register(CabsOnlineForm)
class CabsOnlineFormAdmin(admin.ModelAdmin):
    list_display = ("customer_name","customer_email","mo_no","cab_type","from_destination","to_destination","journey_date","journey_time","datetime")
    list_filter = ('cab_type','from_destination',"to_destination","datetime","journey_time","journey_date")
    search_fields = ("customer_name","customer_email","mo_no","cab_type","from_destination","to_destination","datetime","journey_time","journey_date")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    list_display = ("name","offer","date","sedan","suv","hatchback","xuv","luxury")
    list_filter = ("name","offer","date","sedan","suv","hatchback","xuv","luxury")
    search_fields = ("name","offer","date","sedan","suv","hatchback","xuv","luxury")