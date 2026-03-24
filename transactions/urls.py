from django.urls import path
from .views import (
    TransactionCreateView,
    TransactionListView,
    TransactionUpdateView,
    TransactionDeleteView
)

urlpatterns = [

    path('', TransactionListView.as_view(), name='transactions_list'),

    path('add/', TransactionCreateView.as_view(), name='add_transaction'),

    path('edit/<int:pk>/', TransactionUpdateView.as_view(), name='edit_transaction'),

    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='delete_transaction'),
]