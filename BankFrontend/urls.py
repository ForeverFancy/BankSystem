from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('dist/index.html', views.dist_index)
]
