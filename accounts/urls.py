from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
"""path('profile/edit/', views.profile_edit, name='profile_edit'),"""