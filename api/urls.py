from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArrayDiagonaleView.as_view(), name='api-route'),
]
