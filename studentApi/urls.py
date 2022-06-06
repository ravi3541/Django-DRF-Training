from django.urls import path

from studentApi.views import *


urlpatterns = [
    path('student/',StudentList.as_view()),
    path('student/<int:pk>',StudentDetail.as_view()),
    path('course/',CourseList.as_view()),
    path('course/<int:pk>',CourseDetail.as_view())
]