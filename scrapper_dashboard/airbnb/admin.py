from django.contrib import admin
from .models import HostsModel, PropertyModel, ReviewsModel, RequestTracker


class PropertyInline(admin.TabularInline):
    model = PropertyModel
    extra = 1
    fields = ('property_id', 'property_name', 'country', 'state', 'city', 'rating', 'price')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HostsModel)
class HostsModelAdmin(admin.ModelAdmin):
    list_display = ('host_id', 'host_name', 'number_of_reviews', 'rating', 'years_hosting', 'is_super_host', 'is_verified', 'updated_at', 'created_at')
    search_fields = ('host_id', 'host_name')
    inlines = [PropertyInline]


@admin.register(PropertyModel)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'property_name', 'country', 'state', 'city', 'rating', 'price', 'currency_code', 'latitude', 'longitude', 'host_id', 'updated_at', 'created_at')
    search_fields = ('property_id', 'property_name', 'country', 'state', 'city')
    list_filter = ('country', 'state', 'city')
    
    related_lookup_fields = {
        'fk': ['host_id'],
    }

@admin.register(ReviewsModel)
class ReviewsModelAdmin(admin.ModelAdmin):
    list_display = ('property', 'review_id', 'reviewer_name', 'review_date', 'rating', 'language', 'updated_at', 'created_at')
    search_fields = ('review_id', 'reviewer_name', 'property__property_name')
    list_filter = ('rating', 'language', 'review_date')


@admin.register(RequestTracker)
class RequestTrackerAdmin(admin.ModelAdmin):
    list_display = ('url', 'referer', 'status_code', 'method', 'updated_at', 'created_at')
    search_fields = ('url', 'referer')
    list_filter = ('status_code', 'method')
