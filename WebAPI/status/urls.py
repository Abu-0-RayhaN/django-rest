from django.urls import path
from .views import*
urlpatterns = [
    path('status/',StatusListCreateView.as_view()),
    path('status/<id>/',StatusDetailUpdateDeleteAPIView.as_view()),
]
