from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from places.api.permissions import (IsAuthorOrReadOnly,
                                    IsOwnReviewOrReadOnly)
from places import models
from . import serializers
from drf_multiple_model.views import FlatMultipleModelAPIView
                                    
from rest_framework.pagination import CursorPagination


class CursorSetPagination(CursorPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    ordering = "-created_at"


class RestaurantIdViewset(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantIdSerializer


class RestaurantReviewViewset(viewsets.ModelViewSet):
    queryset = models.RestaurantReview.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.RestaurantReviewGETSerializer
        else:
            return serializers.RestaurantReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = CursorSetPagination

    def perform_create(self, serializer):
        serializer.save(review_author=self.request.user)


"""
Retrieve all the reviews from a single restaurant
"""
class RestaurantReviewListAPIView(generics.ListAPIView):
    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.RestaurantReview.objects.filter(
                                maps=kwarg_maps).order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.RestaurantReviewGETSerializer
        else:
            return serializers.RestaurantReviewSerializer


"""
Retrieve all the starter pictures
"""
class StarterPicsViewset(viewsets.ModelViewSet):
    queryset = models.StarterPic.objects.all()
    serializer_class = serializers.StarterPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


"""
Retrieve all the main course pictures
"""
class MainPicsViewset(viewsets.ModelViewSet):
    queryset = models.MainPic.objects.all()
    serializer_class = serializers.MainPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


"""
Retrieve all the dessert pictures
"""
class DessertPicsViewset(viewsets.ModelViewSet):
    queryset = models.DessertPic.objects.all()
    serializer_class = serializers.DessertPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


"""
Retrieve all the menu pictures
"""
class MenuPicsViewset(viewsets.ModelViewSet):
    queryset = models.MenuPic.objects.all()
    serializer_class = serializers.MenuPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


"""
Retrieve all the utside pictures
"""
class OutsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.OutsidePic.objects.all()
    serializer_class = serializers.OutsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


"""
Retrieve all the inside pictures
"""
class InsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.InsidePic.objects.all()
    serializer_class = serializers.InsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


"""
Retrieve all the reviews from a single user
"""
class UserReviewListAPIView(generics.ListAPIView):
    serializer_class = serializers.RestaurantReviewSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.RestaurantReview.objects.filter(
                                review_author=kwarg_user)


"""
Retrieve all the starter pictures from a single user
"""
class UserSarterPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.StarterPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.StarterPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


"""
Retrieve all the main course pictures from a single user
"""
class UserMainPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MainPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.MainPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


"""
Retrieve all the dessert pictures from a single user
"""
class UserDessertPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.DessertPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.DessertPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


"""
Retrieve all the menu pictures from a single user
"""
class UserMenuPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MenuPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.MenuPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


"""
Retrieve all the outside pictures from a single user
"""
class UserOutsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.OutsidePicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.OutsidePic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


"""
Retrieve all the inside pictures from a single user
"""
class UserInsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.InsidePicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.InsidePic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


"""
Retrieve all the starter pictures from a single restaurant
"""
class RestaurantStarterPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.StarterPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.StarterPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


"""
Retrieve all the main course pictures from a single restaurant
"""
class RestaurantMainPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MainPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.MainPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


"""
Retrieve all the dessert pictures from a single restaurant
"""
class RestaurantDessertPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.DessertPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.DessertPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


"""
Retrieve all the menu pictures from a single restaurant
"""
class RestaurantMenuPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MenuPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.MenuPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


"""
Retrieve all the outside pictures from a single restaurant
"""
class RestaurantOutsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.OutsidePicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.OutsidePic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


"""
Retrieve all the inside pictures from a single restaurant
"""
class RestaurantInsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.InsidePicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')
        return models.InsidePic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


"""
Retrieve all the pictures from all the reviews
"""
class AllEveryRestPicturesAPIView(FlatMultipleModelAPIView):
    querylist = [
        {'queryset': models.StarterPic.objects.all(),
         'serializer_class': serializers.StarterPicsSerializer},
        {'queryset': models.MainPic.objects.all(),
         'serializer_class': serializers.MainPicsSerializer},
        {'queryset': models.DessertPic.objects.all(),
         'serializer_class': serializers.DessertPicsSerializer},
        {'queryset': models.MenuPic.objects.all(),
         'serializer_class': serializers.MenuPicsSerializer},
        {'queryset': models.OutsidePic.objects.all(),
         'serializer_class': serializers.OutsidePicsSerializer},
        {'queryset': models.InsidePic.objects.all(),
         'serializer_class': serializers.InsidePicsSerializer},
    ]


"""
Retrieve all the pictures from one selected user
"""
class AllUserPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_user = self.kwargs.get('user')

        querylist = (
            {'queryset': models.StarterPic.objects.filter(
                restaurant_review__review_author=kwarg_user),
             'serializer_class': serializers.StarterPicsSerializer},
            {'queryset': models.MainPic.objects.filter(
                restaurant_review__review_author=kwarg_user),
             'serializer_class': serializers.MainPicsSerializer},
            {'queryset': models.DessertPic.objects.filter(
                restaurant_review__review_author=kwarg_user),
             'serializer_class': serializers.DessertPicsSerializer},
            {'queryset': models.MenuPic.objects.filter(
                restaurant_review__review_author=kwarg_user),
             'serializer_class': serializers.MenuPicsSerializer},
            {'queryset': models.OutsidePic.objects.filter(
                restaurant_review__review_author=kwarg_user),
             'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset': models.InsidePic.objects.filter(
                restaurant_review__review_author=kwarg_user),
             'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist


"""
Retrieve all the pictures from one select restaurant
"""
class AllSingleRestPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_maps = self.kwargs.get('maps')

        querylist = (
            {'queryset': models.StarterPic.objects.filter(
                restaurant_review__maps=kwarg_maps),
             'serializer_class': serializers.StarterPicsSerializer},
            {'queryset': models.MainPic.objects.filter(
                restaurant_review__maps=kwarg_maps),
             'serializer_class': serializers.MainPicsSerializer},
            {'queryset': models.DessertPic.objects.filter(
                restaurant_review__maps=kwarg_maps),
             'serializer_class': serializers.DessertPicsSerializer},
            {'queryset': models.MenuPic.objects.filter(
                restaurant_review__maps=kwarg_maps),
             'serializer_class': serializers.MenuPicsSerializer},
            {'queryset': models.OutsidePic.objects.filter(
                restaurant_review__maps=kwarg_maps),
             'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset': models.InsidePic.objects.filter(
                restaurant_review__maps=kwarg_maps),
             'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist


"""
Retrieve all the pictures from a single review
"""
class AllReviewPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_review = self.kwargs.get('review')

        querylist = (
            {'queryset': models.StarterPic.objects.filter(
                restaurant_review=kwarg_review),
             'serializer_class': serializers.StarterPicsSerializer},
            {'queryset': models.MainPic.objects.filter(
                restaurant_review=kwarg_review),
             'serializer_class': serializers.MainPicsSerializer},
            {'queryset': models.DessertPic.objects.filter(
                restaurant_review=kwarg_review),
             'serializer_class': serializers.DessertPicsSerializer},
            {'queryset': models.MenuPic.objects.filter(
                restaurant_review=kwarg_review),
             'serializer_class': serializers.MenuPicsSerializer},
            {'queryset': models.OutsidePic.objects.filter(
                restaurant_review=kwarg_review),
             'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset': models.InsidePic.objects.filter(
                restaurant_review=kwarg_review),
             'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist
