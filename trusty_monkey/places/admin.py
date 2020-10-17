from django.contrib import admin
from places.models import (RestaurantReview, StarterPic,
                           MainPic, DessertPic, MenuPic,
                           OutsidePic, InsidePic, Restaurant)
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(StarterPic)
admin.site.register(MainPic)
admin.site.register(DessertPic)
admin.site.register(MenuPic)
admin.site.register(OutsidePic)
admin.site.register(InsidePic)