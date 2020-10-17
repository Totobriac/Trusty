from places.models import (Restaurant, RestaurantReview,
                           StarterPic, MainPic,
                           DessertPic, MenuPic,
                           OutsidePic, InsidePic)
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Q


class RestaurantIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantReviewGETSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='maps.name',read_only=True)
    restaurant_adress = serializers.CharField(source='maps.adress',read_only=True)
    created_at = serializers.SerializerMethodField()
    review_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = RestaurantReview
        fields = ('id','restaurant_name','restaurant_adress','created_at','review_author','maps')

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d %B, %Y")


class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        field = fields = '__all__'
        

class StarterPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarterPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id: 
            raise serializers.ValidationError('the review belongs to a different user')        
        return value
   

class MainPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id: 
            raise serializers.ValidationError('the review belongs to a different user')        
        return value


class DessertPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DessertPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id: 
            raise serializers.ValidationError('the review belongs to a different user')        
        return value


class MenuPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id: 
            raise serializers.ValidationError('the review belongs to a different user')        
        return value


class OutsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsidePic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id: 
            raise serializers.ValidationError('the review belongs to a different user')        
        return value


class InsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsidePic
        field = fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id: 
            raise serializers.ValidationError('the review belongs to a different user')        
        return value