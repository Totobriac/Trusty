from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),    
    path('accounts/register/', RegistrationView.as_view(
                                success_url='/'),
                                name='django_registration_register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.api.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('places.api.urls')),    
    re_path(r"^(?!media).*$", IndexTemplateView.as_view(), name="entry-point"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
