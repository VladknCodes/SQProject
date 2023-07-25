from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


from django.contrib.auth.decorators import login_required


from Supplier_Qualification.models import DRA



# Страница администрирования базы данных
# --------------------------------------------------------------------------------------------------------------
# Страница DRA Supplier list - Таблица DRA (данные по аудиту достоверности данных) Start------------------------
# --------------------------------------------------------------------------------------------------------------

# Получение данных из БД-DRA
@login_required
def viewdra(request):
    supplierlist = DRA.objects.all()
    return render(request, "viewdra.html", {"supplierlist": supplierlist})


# Сохранение данных в БД-DRA
@login_required
def createdra(request):
    if request.method == "POST":
        supplier = DRA()
        supplier.numberItem = request.POST.get("numberItem")
        supplier.numberOrd = request.POST.get("numberOrd")
        supplier.dateOrd = request.POST.get("dateOrd")
        supplier.supplier = request.POST.get("supplier")
        supplier.supplierinfo = request.POST.get("supplierinfo")
        supplier.procedureProc = request.POST.get("procedureProc")
        supplier.purchasedProd = request.POST.get("purchasedProd")
        supplier.dateAudit = request.POST.get("dateAudit")
        supplier.auditResult = request.POST.get("auditResult")
        supplier.numberAudit = request.POST.get("numberAudit")
        supplier.comment = request.POST.get("comment")
        supplier.auditors = request.POST.get("auditors")
        

        supplier.save()
    return HttpResponseRedirect("/viewdra")


# Изменение данных в БД-DRA
@login_required
def editdra(request, id):
    try:
        supplier = DRA.objects.get(id=id)
 
        if request.method == "POST":
            supplier.numberItem = request.POST.get("numberItem")
            supplier.numberOrd = request.POST.get("numberOrd")
            supplier.dateOrd = request.POST.get("dateOrd")
            supplier.supplier = request.POST.get("supplier")
            supplier.supplierinfo = request.POST.get("supplierinfo")
            supplier.procedureProc = request.POST.get("procedureProc")
            supplier.purchasedProd = request.POST.get("purchasedProd")
            supplier.dateAudit = request.POST.get("dateAudit")
            supplier.auditResult = request.POST.get("auditResult")
            supplier.numberAudit = request.POST.get("numberAudit")
            supplier.comment = request.POST.get("comment")
            supplier.auditors = request.POST.get("auditors")
            
            supplier.save()
            return HttpResponseRedirect("/viewdra")
        else:
            return render(request, "editdra.html", {"supplier": supplier})
    except DRA.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")


# Удаление данных из БД-DRA
@login_required
def deletedra(request, id):
    try:
        supplier = DRA.objects.get(id=id)
        supplier.delete()
        return HttpResponseRedirect("/viewdra")
    except DRA.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")

# --------------------------------------------------------------------------------------------------------------
# Страница DRA Supplier list - Таблица DRA End------------------------------------------------------------------
