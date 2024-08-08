from django.db import models


class HostsModel(models.Model):
    host_id = models.CharField(max_length=50, primary_key=True)
    host_name = models.CharField(max_length=50)
    number_of_reviews = models.IntegerField()
    rating = models.FloatField()
    years_hosting = models.IntegerField()
    is_super_host = models.BooleanField()
    is_verified = models.BooleanField()
    profile_image = models.CharField(max_length=500)
    about = models.TextField()
    host_details = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'host'
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'

    def __str__(self):
        return self.host_name

class PropertyModel(models.Model):
    property_id = models.CharField(max_length=50, primary_key=True)
    property_name = models.CharField(max_length=256)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    amenities = models.JSONField()
    room_arrangement = models.JSONField()
    rating = models.FloatField()
    detailed_review = models.JSONField()
    number_of_reviews = models.IntegerField()
    images = models.JSONField()
    price = models.FloatField()
    currency_code = models.CharField(max_length=5)
    facilities = models.JSONField()
    policies = models.JSONField()
    host = models.ForeignKey(HostsModel, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'property'
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.property_name

class ReviewsModel(models.Model):
    property = models.ForeignKey(PropertyModel, on_delete=models.CASCADE)
    review_id = models.CharField(max_length=100, primary_key=True)
    reviewer_name = models.CharField(max_length=50)
    comments = models.TextField()
    profile_image_url = models.CharField(max_length=1000)
    review_date = models.DateTimeField()
    reviewer_location = models.CharField(max_length=100)
    rating = models.FloatField()
    language = models.CharField(max_length=5)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class RequestTracker(models.Model):
    url = models.CharField(max_length=5000, primary_key=True)
    referer = models.CharField(max_length=5000, blank=True, null=True)
    status_code = models.IntegerField()
    method = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'request_tracker'
        verbose_name = 'Request Tracker'
        verbose_name_plural = 'Request Trackers'
