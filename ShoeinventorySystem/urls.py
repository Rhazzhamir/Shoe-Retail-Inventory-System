


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls' )),
    path('accounts/' , include('accounts.urls')),
    path('user/', include('user.urls')),
    path('seller/' , include('seller.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)