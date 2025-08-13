from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index, contact

urlpatterns =[
    path('items/', include('item.urls')),
    path('dashboard/', include ('dashboard.urls')),
    path('', include ('core.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)