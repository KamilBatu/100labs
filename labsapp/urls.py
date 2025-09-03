from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('download/windows/', views.download_windows, name='download_windows'),
]


