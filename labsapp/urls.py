from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('download/windows/', views.download_windows, name='download_windows'),
    path('assets/scene.json', views.lottie_scene, name='lottie_scene'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]


