from django.shortcuts import render
import datetime
from .forms import *


def landing(request):
    name = 'Dima'
    form = SubscriberFrom(request.POST or None)
    date = datetime.datetime.now().strftime('%Y')

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

        print(request.POST)
        print(form.cleaned_data)


    return render(request,'landing/landing.html', locals())