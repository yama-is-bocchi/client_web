from django.views import generic
from client_web_project.models import *
from client_web_project.form import WordForm
from django.shortcuts import *
import random
import time

def index(request):
    return render(request, 'client_web_project/index.html')


def start_game(request):
    word_class=Word.objects.all()
    pks=word_class.order_by('?')[:4]
    pks_list=list(pks)
    if len(pks)<4:
        return render(request, 'client_web_project/index.html')
    else:
        imi=pks_list
        none=random.sample(imi,len(imi))
        p_list=pks_list+none
        return render(request, 'client_web_project/main.html', {'word_list': p_list})

def start_eng_game(request):
    word_class=Word.objects.all()
    pks=word_class.order_by('?')[:4]
    pks_list=list(pks)
    if len(pks)<4:
        return render(request, 'client_web_project/index.html')
    else:
        imi=pks_list
        none=random.sample(imi,len(imi))
        p_list=pks_list+none
        return render(request, 'client_web_project/main_two.html', {'word_list': p_list})
