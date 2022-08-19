from django.urls import path
from .views import SinglePerfumeView, ListPerfumeView

urlpatterns = [
    path('', ListPerfumeView.as_view()),
    path('<int:pk>/', SinglePerfumeView.as_view()),
]