from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
        	'opening_time',
        	'closing_time',
        	]
class DetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['owner','name', 'description', 'opening_time', 'closing_time','id']
		
class RestaurantUpdateListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		exclude = ['logo', 'owner']
