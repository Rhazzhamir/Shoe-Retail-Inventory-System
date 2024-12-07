



from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('accounts.urls')),
    path('user/', include('user.urls')),
    path('seller/' , include('seller.urls')),
]
