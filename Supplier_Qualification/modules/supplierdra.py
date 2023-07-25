from django.shortcuts import render

from Supplier_Qualification.models import DRA

import os



# Функция загрузки страницы поставщика - DRA по номеру заявки---------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

def supplierdra(request, id):

    try:
        supplier = DRA.objects.get(numberOrd=id)

        
        # Формирование списка файлов - DRA
        
        link_files = "/static/files/dra/" + str(supplier.numberOrd) + "/"
        dirPath = "..\\static\\files\\dra\\" + str(supplier.numberOrd)
        
        # Получение списка имен файлов в дереве каталога
        files = next(os.walk(dirPath))[2]


        return render(request, "supplierdra.html", {
            'title' : supplier.supplier,
            'supplier' : supplier,
            'supplier.supplierinfo' : supplier.supplierinfo,
            'files' : files,
            'link_files' : link_files})

    
    # При отсутвии в БД поставщика с данным запросом - Вывод информации на экран
    except DRA.DoesNotExist:

        supplierContent = "Supplier not found"

        return render(request, "supplierdra_er.html", {'supplierContent' : supplierContent})
