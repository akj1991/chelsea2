from django.urls import path
from . import views
urlpatterns = [
    path('1st/',views.index),
    path('2nd/',views.index2),
]