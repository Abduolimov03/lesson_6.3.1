from django.urls import path
from .views import mobile

urlpatterns = [
    path('mobile/', mobile, name='mobile')
]