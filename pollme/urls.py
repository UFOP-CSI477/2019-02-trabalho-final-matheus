from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('polls/', include('polls.urls', namespace='polls')),
    path('accounts/', include('accounts.urls', namespace="accounts"))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
