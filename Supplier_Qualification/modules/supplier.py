from django.shortcuts import render

from Supplier_Qualification.models import Supplier
from Supplier_Qualification.models import Product

import os



# Функция загрузки страницы поставщика по ID -------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

def supplier(request, id):

    try:
        supplier = Supplier.objects.get(id=id)

      
        # Получение из дочерней таблицы "Product" данных по продуктовой аттестации по определённому поставщику
        products_list = Product.objects.filter(supplier__id=supplier.id)
        prod_txt = ""
       
        for product in products_list:
            prod_txt = prod_txt + """<div>""" + product.prodName +": " + product.prodStatus + " " + product.statusData + """</div>"""

        
        # Формирование списка файлов - CQ и PQ
        
        link_files_cq = "/static/files/cqpq/" + str(supplier.id) + "/" + "cq" + "/"
        link_files_pq = "/static/files/cqpq/" + str(supplier.id) + "/" + "pq" + "/"

        dirPathCQ = "..\\static\\files\\cqpq\\" + str(supplier.id) + "\\cq"
        dirPathPQ = "..\\static\\files\\cqpq\\" + str(supplier.id) + "\\pq"
        
        # Получение списков имен файлов в дереве каталогов
        filesCQ = next(os.walk(dirPathCQ))[2]
        filesPQ = next(os.walk(dirPathPQ))[2]
                
        
        return render(request, "supplier.html", {
            'title' : supplier.name,
            'supplier.supplierinfo' : supplier.supplierinfo,
            'supplier' : supplier,
            'prod_txt' : prod_txt,
            'filesCQ' : filesCQ,
            'filesPQ' : filesPQ,
            'link_files_cq' : link_files_cq,
            'link_files_pq' : link_files_pq})
            
    # При отсутвии в БД поставщика с данным запросом - Вывод информации на экран
    except Supplier.DoesNotExist:

        supplierContent = "Supplier not found"

        return render(request, "supplier_er.html", {'supplierContent' : supplierContent})
