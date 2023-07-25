# Supplier Qualification Portal.
# Developed by Kartashov Vladislav.
# 2023.


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


from .models import DRA
from .models import News
from .models import DRAauditors



# DRF
from .serializers import NewsSerializer
from rest_framework import generics


# Импортируемые модули
from .modules.lqs import *
from .modules.adddef import *
from .modules.viewprod import *
from .modules.viewdra import *
from .modules.viewdb import *
from .modules.viewdbsp import *
from .modules.printtablelist import *
from .modules.supplier import *
from .modules.supplierdra import *




# DRF
class NewsListCreate(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer





# Функции страниц сайта Start-----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# DRF
def appnews(request):
    return render(request, "appnews.html", {'title' : "News"})

def qualification_status(request):
    splist = printtablelist ()
    return render(request, "qualification_status.html", {'title' : "Qualification status", 'splist' : splist})

def audit_schedule(request):
    return render(request, "audit_schedule.html", {'title' : "Audit schedule"})

def qprocess(request):
    return render(request, "qprocess.html", {'title' : "Qualification process"})

def dra(request):
    supplierlist = DRA.objects.all()
    return render(request, "dra.html", {'title' : "Аудит достоверности данных", 'supplierlist' : supplierlist})

def draauditors(request):
    auditors = DRAauditors.objects.all()
    return render(request, "draauditors.html", {'title' : "Аудит достоверности данных - Реестр аудиторов", 'auditors' : auditors})


# --------------------------------------------------------------------------------------------------------------
# Функции страниц сайта End-------------------------------------------------------------------------------------
