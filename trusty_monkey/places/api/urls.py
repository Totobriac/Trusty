from django.urls import include, path
from rest_framework import routers
from places.api import views

router = routers.DefaultRouter()
router.register(r'restaurant', views.RestaurantIdViewset)
router.register(r'restaurant_review', views.RestaurantReviewViewset)
router.register(r'starter_pic', views.StarterPicsViewset)
router.register(r'main_pic', views.MainPicsViewset)
router.register(r'dessert_pic', views.DessertPicsViewset)
router.register(r'menu_pic', views.MenuPicsViewset)
router.register(r'outside_pic', views.OutsidePicsViewset)
router.register(r'inside_pic', views.InsidePicsViewset)

urlpatterns = [
    path('', include(router.urls)),   
    path('user_review/<int:user>/',
                views.UserReviewListAPIView.as_view(),
                name='review_by_user'),
    path('rest_review/<str:maps>/',
                views.RestaurantReviewListAPIView.as_view(),
                name='review_by_restaurant'),
    path('user_starter_pic/<int:user>/', 
                views.UserSarterPicsListAPIView.as_view(),
                name='user_starter_pic'),
    path('user_main_pic/<int:user>/',
                views.UserMainPicsListAPIView.as_view(),
                name='user_main_pic'),
    path('user_dessert_pic/<int:user>/',
                views.UserDessertPicsListAPIView.as_view(),
                name='user_dessert_pic'),
    path('user_menu_pic/<int:user>/',
                views.UserMenuPicsListAPIView.as_view(),
                name='user_menu_pic'),
    path('user_outside_pic/<int:user>/',
                views.UserOutsidePicsListAPIView.as_view(),
                name='user_outside_pic'),
    path('user_inside_pic/<int:user>/',
                views.UserInsidePicsListAPIView.as_view(),
                name='user_inside_pic'),
    path('rest_starter_pic/<str:maps>/',
                views.RestaurantStarterPicsListAPIView.as_view(), 
                name='rest_starter_pic'),
    path('rest_main_pic/<str:maps>/', 
                views.RestaurantMainPicsListAPIView.as_view(), 
                name='rest_main_pic'),
    path('rest_dessert_pic/<str:maps>/', 
                views.RestaurantDessertPicsListAPIView.as_view(),
                name='rest_dessert_pic'),
    path('rest_menu_pic/<str:maps>/',
                views.RestaurantMenuPicsListAPIView.as_view(),
                name='rest_menu_pic'),
    path('rest_outside_pic/<str:maps>/',
                views.RestaurantOutsidePicsListAPIView.as_view(),
                name='rest_outside_pic'),
    path('rest_inside_pic/<str:maps>/',
                views.RestaurantInsidePicsListAPIView.as_view(),
                name='rest_inside_pic'),

    path('all_pics/',
                views.AllEveryRestPicturesAPIView.as_view(),
                name='show_all_pictures'),
    path('all_user_pics/<int:user>/',
                views.AllUserPicturesAPIView.as_view(),
                name='show_all_user_pictures'),
    path('all_single_rest_pics/<str:maps>/',
                views.AllSingleRestPicturesAPIView.as_view(),
                name='show_all_single_rest_pictures'),
    path('every_review_pics/<int:review>/',
                views.AllReviewPicturesAPIView.as_view(),
                name='show_all_review_pictures'),
]

