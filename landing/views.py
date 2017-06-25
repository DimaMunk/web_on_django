from django.shortcuts import render
import datetime
from .forms import *


def landing(request):
    # name = 'Dima'
    # date = datetime.datetime.now().strftime('%Y')
    form = SubscriberFrom(request.POST or None)
    

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

        # print(request.POST)
        # print(form.cleaned_data)


    return render(request,'landing/landing.html', locals())