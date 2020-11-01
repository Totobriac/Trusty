from places.models import (Restaurant, RestaurantReview,
                           StarterPic, MainPic,
                           DessertPic, MenuPic,
                           OutsidePic, InsidePic)
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Q

"""
Serializer for restaurant instance
"""
class RestaurantIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


"""
Serializer for restaurant reviews when GET method is used
"""
class RestaurantReviewGETSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='maps.name',
                                            read_only=True)
    restaurant_adress = serializers.CharField(source='maps.adress',
                                              read_only=True)
    created_at = serializers.SerializerMethodField()
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RestaurantReview
        fields = ('id', 'restaurant_name', 'restaurant_adress',
                  'created_at', 'review_author', 'maps')

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d %B, %Y")


"""
Serializer for restaurant reviews for any except GET method is used
"""
class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        field = fields = '__all__'


"""
Serializer for starter pics model
"""
class StarterPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarterPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id:
            raise serializers.ValidationError(
                'the review belongs to a different user')
        return value


"""
Serializer for main course pics model
"""
class MainPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id:
            raise serializers.ValidationError(
                'the review belongs to a different user')
        return value


"""
Serializer for dessert pics model
"""
class DessertPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DessertPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id:
            raise serializers.ValidationError(
                'the review belongs to a different user')
        return value


"""
Serializer for menu pics model
"""
class MenuPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id:
            raise serializers.ValidationError(
                'the review belongs to a different user')
        return value


"""
Serializer for outside pics model
"""
class OutsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsidePic
        fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id:
            raise serializers.ValidationError(
                'the review belongs to a different user')
        return value


"""
Serializer for inside  pics model
"""
class InsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsidePic
        field = fields = '__all__'

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
        if user.pk != value.review_author_id:
            raise serializers.ValidationError(
                'the review belongs to a different user')
        return value
