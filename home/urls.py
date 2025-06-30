from django.urls import path
from .views import home, contact, news

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news')
]