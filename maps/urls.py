from django.urls import path                                                                                                                              
from . import views

urlpatterns = [ 
    path(r'', views.index, name="map"),
    path(r'mapbox-token/', views.get_mapbox_token, name="mapbox-token"),
    path(r'random-location/', views.get_random_location, name="random-location"),
]