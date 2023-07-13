from django.urls import path
from .views import speciality_list, subjects_list, subject_detail, speciality_detail

urlpatterns = [
    path('speciality/', speciality_list, name='specialities-list'),
    path('speciality/<int:pk>/', speciality_detail, name='speciality-detail'),
    path('subject/', subjects_list, name='subjects-list'),
    path('subject/<int:pk>/', subject_detail, name='subject-detail'),
]