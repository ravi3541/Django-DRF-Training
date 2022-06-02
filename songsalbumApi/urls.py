from django.urls import path
from songsalbumApi import views

urlpatterns = [
    path('singer/',views.Singer_list),
    path('singer/<int:pk>/', views.Singer_detail),
    path('song/',views.Song_list),
    path('song/<int:pk>/',views.Song_detail)
]