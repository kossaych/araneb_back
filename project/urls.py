from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('manager/',include('manager.urls')),

    #path('accounts/', include('django.contrib.auth.urls')),
    #auth urls
    #path('api-token-auth',obtain_auth_token),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
