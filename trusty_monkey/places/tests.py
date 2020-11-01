
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import (DessertPic, InsidePic,
                     MainPic, MenuPic, OutsidePic,
                     Restaurant, RestaurantReview, StarterPic)

"""
Testing if user can create an account
"""
class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "TotoBriac", "email": "toto@gmail.com",
                "password1": "strongPsw", "password2": "strongPsw"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "TotoBriac")

"""
Testing if a restaurant can be created from Google Places API data
"""
class CreateRestaurantTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="TotoBriac",
                                             email="toto@gmail.com",
                                             password="strongPsw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_restaurant(self):
        self.data = {"maps": "ChIJd230zfzz5URz8XVIZjiVzYc",
                     "name": "Les Fricoteurs",
                     "opened": ["lundi à samedi"], "website": "fricoteurs.com",
                     "phone": "010203040506", "restLat": 0.1,
                     "restLng": 0.1, "adress": "21 grande rue"}
        response = self.client.post("/api/restaurant/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().maps,
                         "ChIJd230zfzz5URz8XVIZjiVzYc")
        self.assertEqual(Restaurant.objects.get().name, "Les Fricoteurs")
        self.assertEqual(Restaurant.objects.get().opened, ["lundi à samedi"])
        self.assertEqual(Restaurant.objects.get().website, "fricoteurs.com")
        self.assertEqual(Restaurant.objects.get().phone, "010203040506")
        self.assertEqual(Restaurant.objects.get().restLat, 0.1)
        self.assertEqual(Restaurant.objects.get().restLng, 0.1)
        self.assertEqual(Restaurant.objects.get().adress, "21 grande rue")

"""
Testing if a review can be created from an existing restaurant
"""
class CreateReviewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="TotoBriac",
                                             email="toto@gmail.com",
                                             password="strongPsw")
        self.restaurant = Restaurant.objects.create(
                                            maps="ChIJd230zfzz5URz8XVIZjiVzYc",
                                            name="Les Fricoteurs",
                                            opened=["lundi à samedi"],
                                            website="fricoteurs.com",
                                            phone="010203040506",
                                            restLat=0.1,
                                            restLng=0.1,
                                            adress="21 grande rue")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_review(self):
        self.data = {"maps": "ChIJd230zfzz5URz8XVIZjiVzYc",
                     "review_author": self.user.id}
        response = self.client.post("/api/restaurant_review/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RestaurantReview.objects.count(), 1)

"""
Testing if a picture can be uploaded in a review in any category
"""
class AddPicsTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="TotoBriac",
                                             email="toto@gmail.com",
                                             password="strongPsw")
        self.restaurant = Restaurant.objects.create(
                                            maps="ChIJd230zfzz5URz8XVIZjiVzYc",
                                            name="Les Fricoteurs",
                                            opened=["lundi à samedi"],
                                            website="fricoteurs.com",
                                            phone="010203040506",
                                            restLat=0.1,
                                            restLng=0.1,
                                            adress="21 grande rue")
        self.restaurant_review = RestaurantReview.objects.create(
                                            maps=self.restaurant,
                                            review_author=self.user)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_add_starter_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id,
                     "picture_1": SimpleUploadedFile(
                        name='starter_pic.jpg',
                        content=open("./staticfiles/banane_seule.jpg",
                                     'rb').read(),
                        content_type='image/jpeg')}
        response = self.client.post("/api/starter_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_main_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id,
                     "picture_1": SimpleUploadedFile(
                        name='main_pic.jpg',
                        content=open("./staticfiles/banane_seule.jpg",
                                     'rb').read(),
                        content_type='image/jpeg')}
        response = self.client.post("/api/main_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_dessert_pic(self):
        print(self.restaurant_review.id)
        self.data = {"restaurant_review": self.restaurant_review.id,
                     "picture_1": SimpleUploadedFile(
                        name='dessert_pic.jpg',
                        content=open("./staticfiles/banane_seule.jpg",
                                     'rb').read(),
                        content_type='image/jpeg')}
        print(self.data)
        response = self.client.post("/api/dessert_pic/", data=self.data)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_menu_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id,
                     "picture_1": SimpleUploadedFile(
                        name='menu_pic.jpg',
                        content=open("./staticfiles/banane_seule.jpg",
                                     'rb').read(),
                        content_type='image/jpeg')}
        response = self.client.post("/api/menu_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_outside_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id,
                     "picture_1": SimpleUploadedFile(
                        name='outside_pic.jpg',
                        content=open("./staticfiles/banane_seule.jpg",
                                     'rb').read(),
                        content_type='image/jpeg')}
        response = self.client.post("/api/outside_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_inside_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id,
                     "picture_1": SimpleUploadedFile(
                        name='inside_pic.jpg',
                        content=open("./staticfiles/banane_seule.jpg",
                                     'rb').read(),
                        content_type='image/jpeg')}
        response = self.client.post("/api/inside_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

"""
Testing if a picture can be retrieved from any category in a review
"""
class GetPicsTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="TotoBriac",
                                             email="toto@gmail.com",
                                             password="strongPsw")
        self.restaurant = Restaurant.objects.create(
                                            maps="ChIJd230zfzz5URz8XVIZjiVzYc",
                                            name="Les Fricoteurs",
                                            opened=["lundi à samedi"],
                                            website="fricoteurs.com",
                                            phone="010203040506",
                                            restLat=0.1,
                                            restLng=0.1,
                                            adress="21 grande rue")
        self.restaurant_review = RestaurantReview.objects.create(
                                            maps=self.restaurant,
                                            review_author=self.user)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.starterPic = StarterPic.objects.create(
                          restaurant_review=self.restaurant_review,
                          picture_1=SimpleUploadedFile(
                            name='starter_pic.jpg',
                            content=open("./staticfiles/banane_seule.jpg",
                                         'rb').read(),
                            content_type='image/jpeg'))
        self.mainPic = MainPic.objects.create(
                       restaurant_review=self.restaurant_review,
                       picture_1=SimpleUploadedFile(
                            name='main_pic.jpg',
                            content=open("./staticfiles/banane_seule.jpg",
                                         'rb').read(),
                            content_type='image/jpeg'))
        self.dessertPic = DessertPic.objects.create(
                            restaurant_review=self.restaurant_review,
                            picture_1=SimpleUploadedFile(
                                name='dessert_pic.jpg',
                                content=open("./staticfiles/banane_seule.jpg",
                                             'rb').read(),
                                content_type='image/jpeg'))
        self.menuPic = MenuPic.objects.create(
                            restaurant_review=self.restaurant_review,
                            picture_1=SimpleUploadedFile(
                                name='menu_pic.jpg',
                                content=open("./staticfiles/banane_seule.jpg",
                                             'rb').read(),
                                content_type='image/jpeg'))
        self.insidePic = InsidePic.objects.create(
                            restaurant_review=self.restaurant_review,
                            picture_1=SimpleUploadedFile(
                                name='inside_pic.jpg',
                                content=open("./staticfiles/banane_seule.jpg",
                                             'rb').read(),
                                content_type='image/jpeg'))
        self.outsidePic = OutsidePic.objects.create(
                            restaurant_review=self.restaurant_review,
                            picture_1=SimpleUploadedFile(
                                name='outside_pic.jpg',
                                content=open("./staticfiles/banane_seule.jpg",
                                             'rb').read(),
                                content_type='image/jpeg'))

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_every_starter_pic(self):
        response = self.client.get("/api/starter_pic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_every_main_pic(self):
        response = self.client.get("/api/main_pic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_every_dessert_pic(self):
        response = self.client.get("/api/dessert_pic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_every_menu_pic(self):
        response = self.client.get("/api/menu_pic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_every_inside_pic(self):
        response = self.client.get("/api/inside_pic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_every_outside_pic(self):
        response = self.client.get("/api/outside_pic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_starter_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id}
        response = self.client.get("/api/starter_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_main_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id}
        response = self.client.get("/api/main_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_dessert_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id}
        response = self.client.get("/api/dessert_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_menu_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id}
        response = self.client.get("/api/menu_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_outside_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id}
        response = self.client.get("/api/outside_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_inside_pic(self):
        self.data = {"restaurant_review": self.restaurant_review.id}
        response = self.client.get("/api/inside_pic/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
