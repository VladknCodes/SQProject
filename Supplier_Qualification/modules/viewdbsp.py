from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


from django.contrib.auth.decorators import login_required

from Supplier_Qualification.models import Supplier



# Страница администрирования базы данных
# --------------------------------------------------------------------------------------------------------------
# Страница Supplier list - Таблица Supplier (данные по аттестации поставщиков) Start----------------------------
# --------------------------------------------------------------------------------------------------------------

# Получение данных из БД
@login_required
def viewdbsp(request):
    supplierlist = Supplier.objects.all()
    return render(request, "viewdbsp.html", {"supplierlist": supplierlist})


# Сохранение данных в БД
@login_required
def createsp(request):
    if request.method == "POST":
        supplier = Supplier()
        supplier.name = request.POST.get("name")
        supplier.supplierinfo = request.POST.get("supplierinfo")
        supplier.cq = request.POST.get("cq")
        supplier.cqdata = request.POST.get("cqdata")
        supplier.audited = request.POST.get("audited")

        supplier.save()
    return HttpResponseRedirect("/viewdbsp")


# Изменение данных в БД
@login_required
def editsp(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
 
        if request.method == "POST":
            supplier.name = request.POST.get("name")
            supplier.supplierinfo = request.POST.get("supplierinfo")
            supplier.cq = request.POST.get("cq")
            supplier.cqdata = request.POST.get("cqdata")
            supplier.audited = request.POST.get("audited")

            supplier.save()
            return HttpResponseRedirect("/viewdbsp")
        else:
            return render(request, "editsp.html", {"supplier": supplier})
    except Supplier.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")


# Удаление данных из БД
@login_required
def deletesp(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
        supplier.delete()
        return HttpResponseRedirect("/viewdbsp")
    except Supplier.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")

# --------------------------------------------------------------------------------------------------------------
# Страница Supplier list - Таблица Supplier End-----------------------------------------------------------------
