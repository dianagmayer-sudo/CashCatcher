from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView
)

urlpatterns = [

    path('', CategoryListView.as_view(), name='categories_list'),

    path('add/', CategoryCreateView.as_view(), name='add_category'),

    path('edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),

    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

]