from django.urls import path
from .views import HomePageView, AboutPageView, BasePageView

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]