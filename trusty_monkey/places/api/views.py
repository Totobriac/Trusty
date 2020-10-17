from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from places.api.permissions import (IsAuthorOrReadOnly,
                                    IsOwnReviewOrReadOnly)
from places import models
from . import serializers
from drf_multiple_model.views import (FlatMultipleModelAPIView,
                                    ObjectMultipleModelAPIView)
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

    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    pagination_class = CursorSetPagination

    def perform_create(self, serializer):
        serializer.save(review_author=self.request.user)
        

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


class StarterPicsViewset(viewsets.ModelViewSet):
    queryset = models.StarterPic.objects.all()
    serializer_class = serializers.StarterPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


class MainPicsViewset(viewsets.ModelViewSet):
    queryset = models.MainPic.objects.all()
    serializer_class = serializers.MainPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

       
class DessertPicsViewset(viewsets.ModelViewSet):
    queryset = models.DessertPic.objects.all()
    serializer_class = serializers.DessertPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

    
class MenuPicsViewset(viewsets.ModelViewSet):
    queryset = models.MenuPic.objects.all()
    serializer_class = serializers.MenuPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

    
class OutsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.OutsidePic.objects.all()
    serializer_class = serializers.OutsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

    
class InsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.InsidePic.objects.all()
    serializer_class = serializers.InsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


class UserReviewListAPIView(generics.ListAPIView):
    serializer_class = serializers.RestaurantReviewSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.RestaurantReview.objects.filter(
                                review_author=kwarg_user)


class UserSarterPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.StarterPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.StarterPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserMainPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MainPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.MainPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserDessertPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.DessertPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.DessertPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserMenuPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MenuPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.MenuPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserOutsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.OutsidePicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.OutsidePic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserInsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.InsidePicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.InsidePic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class RestaurantStarterPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.StarterPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')       
        return models.StarterPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


class RestaurantMainPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MainPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')       
        return models.MainPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


class RestaurantDessertPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.DessertPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')       
        return models.DessertPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


class RestaurantMenuPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MenuPicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')       
        return models.MenuPic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


class RestaurantOutsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.OutsidePicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')       
        return models.OutsidePic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


class RestaurantInsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.InsidePicsSerializer

    def get_queryset(self):
        kwarg_maps = self.kwargs.get('maps')       
        return models.InsidePic.objects.filter(
                                restaurant_review__maps=kwarg_maps)


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


class AllUserPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_user = self.kwargs.get('user')

        querylist = (
            {'queryset': 
            models.StarterPic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.StarterPicsSerializer},
            {'queryset':
            models.MainPic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.MainPicsSerializer},
            {'queryset': 
            models.DessertPic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.DessertPicsSerializer},
            {'queryset': 
            models.MenuPic.objects.filter(restaurant_review__review_author=kwarg_user),    
                        'serializer_class': serializers.MenuPicsSerializer},
            {'queryset': 
            models.OutsidePic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset': 
            models.InsidePic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist


class AllSingleRestPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_maps = self.kwargs.get('maps')

        querylist = (
            {'queryset':
            models.StarterPic.objects.filter(restaurant_review__maps=kwarg_maps),
                        'serializer_class': serializers.StarterPicsSerializer},
            {'queryset':
            models.MainPic.objects.filter(restaurant_review__maps=kwarg_maps),
                        'serializer_class': serializers.MainPicsSerializer},
            {'queryset':
            models.DessertPic.objects.filter(restaurant_review__maps=kwarg_maps),
                        'serializer_class': serializers.DessertPicsSerializer},
            {'queryset':
            models.MenuPic.objects.filter(restaurant_review__maps=kwarg_maps),
                        'serializer_class': serializers.MenuPicsSerializer},
            {'queryset':
            models.OutsidePic.objects.filter(restaurant_review__maps=kwarg_maps),
                        'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset':
            models.InsidePic.objects.filter(restaurant_review__maps=kwarg_maps),
                        'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist


class AllReviewPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_review = self.kwargs.get('review')

        querylist = (
            {'queryset':
            models.StarterPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.StarterPicsSerializer},
            {'queryset':
            models.MainPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.MainPicsSerializer},
            {'queryset':
            models.DessertPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.DessertPicsSerializer},
            {'queryset':
            models.MenuPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.MenuPicsSerializer},
            {'queryset':
            models.OutsidePic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset':
            models.InsidePic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist
