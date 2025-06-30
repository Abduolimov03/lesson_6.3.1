from django.shortcuts import render
from .models import Mobile

def mobile(request):
    mobile = Mobile.objects.all()
    context = {
        'mobile' : mobile
    }
    return render(request, 'mobile.html', context=context)