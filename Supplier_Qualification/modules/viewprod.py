from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


from django.contrib.auth.decorators import login_required


from Supplier_Qualification.models import Supplier
from Supplier_Qualification.models import Product



# Страница администрирования базы данных
# --------------------------------------------------------------------------------------------------------------
# Страница Product Qalification list
# Дочерняя таблица Product (данные по аттестации продукции к основной таблице Supplier ) Start
# --------------------------------------------------------------------------------------------------------------


# # Получение данных из БД-Product
@login_required
def viewprod(request):
    products = Product.objects.all()
    return render(request, "viewprod.html", {"products": products})
 
# Добавление данных из БД-Product
@login_required
def createprod(request):
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.prodName = request.POST.get("prodName")
        product.prodStatus = request.POST.get("prodStatus")
        product.statusData = request.POST.get("statusData")
        product.supplier_id = request.POST.get("supplier")
        
        product.save()
        return HttpResponseRedirect("/viewprod")
    # передаем данные в шаблон
    suppliers = Supplier.objects.all()
    return render(request, "createprod.html", {"suppliers": suppliers})
 
# Изменение данных в БД-Product
@login_required
def editprod(request, id):
    try:
        product = Product.objects.get(id=id)
 
        if request.method == "POST":
            product.prodName = request.POST.get("prodName")
            product.prodStatus = request.POST.get("prodStatus")
            product.statusData = request.POST.get("statusData")
            product.supplier_id = request.POST.get("supplier")

            product.save()
            return HttpResponseRedirect("/viewprod")
        else:
            suppliers = Supplier.objects.all()
            return render(request, "editprod.html", {"product": product, "suppliers": suppliers})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
     
# Удаление данных из БД-Product 
@login_required
def deleteprod(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/viewprod")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

# Страница Product Qalification list
# Дочерняя таблица Product (данные по аттестации продукции к основной таблице Supplier ) End
# --------------------------------------------------------------------------------------------------------------
