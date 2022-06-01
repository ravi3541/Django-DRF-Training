from django.urls import path
from employeeApi import views


#This app demonstartes Serializers, models, validation,


urlpatterns = [
    path('employee/',views.Employee_list),
    path('employee/<int:pk>/', views.Employee_detail),
    path('project/',views.Project_list),
    path('project/<int:pk>/',views.Project_detail)
]