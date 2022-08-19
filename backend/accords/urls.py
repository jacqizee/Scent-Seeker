from django.urls import path
from .views import ListAccordView, DetailedAccordView

urlpatterns = [
    path('', ListAccordView.as_view(), name='accord-list'),
    path('<int:pk>/', DetailedAccordView.as_view(), name='accord-detailed'),
]