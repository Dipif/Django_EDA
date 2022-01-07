from django.shortcuts import render
from django.urls import reverse
from .forms import MeatForm
from .models import MeatSetting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from io import StringIO
from eda_proj.settings import BASE_DIR


# Create your views here.


def show_meat_price(request) :
    meat_all = MeatSetting.objects.all()
    if request.method == 'POST':
        form = MeatForm(request.POST)
        if form.is_valid() :
            form.save()
    form = MeatForm()
    meat_setting = MeatSetting.objects.last()
    return render(request, 'meatprice.html', {"meat" : meat_setting, "meat_list" : meat_all, "form" : form})


