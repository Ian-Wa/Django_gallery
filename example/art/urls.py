from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.showpage, name= 'showpage'),
    path('search/', views.search_category, name='search_category'),
    re_path(r'^image/(?P<image_id>\d+)/$',views.image_properties, name='image'),
    re_path(r'^location/(?P<location_name>\w+)',views.image_location,name = 'location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)