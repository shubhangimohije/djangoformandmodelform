from django.urls import path
from . import views


urlpatterns = [
    path('dis/', views.dispaly),
    path('stu/',views.view_student, name='stu'),
    path('uni/',views.view_university, name='uni'),

]