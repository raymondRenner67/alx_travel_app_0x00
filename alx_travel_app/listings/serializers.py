from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price', 'host', 'created_at')


class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    guest = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'listing', 'guest', 'start_date', 'end_date', 'total_price', 'status')

    def validate(self, data):
        # ensure end_date >= start_date
        start = data.get('start_date')
        end = data.get('end_date')
        if start and end and end < start:
            raise serializers.ValidationError('end_date must be on or after start_date')
        return data
