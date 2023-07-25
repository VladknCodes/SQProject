from django.http import HttpResponse

from Supplier_Qualification.models import Supplier
from Supplier_Qualification.models import Product

import datetime


################################################################################################################
# Дополнительные функции для работы сайта-----------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# Станица вывода таблицы c данными по аттестации поставщиков Start----------------------------------------------
# --------------------------------------------------------------------------------------------------------------

def printdbsp(request):
    supplierlist = Supplier.objects.in_bulk()

    ttop = """
    <table border="1" cellpadding="4" cellspacing="0">
    <tbody>
    <tr>
      <th>Id</th>
      <th>Supplier</th>
      <th>Supplier Info</th>
      <th>Commercial qualification</th>
      <th>Data</th>
      <th>Product qualification</th>
      <th>Conducted audits and audit teams</th>
    </tr>
    """
    tcenter = ""

    tbottom ="""
    </tbody>
    </table>
    """
        
    
    for id in supplierlist:


        # Получение из дочерней таблицы "Product" данных по продуктовой аттестации по определённому поставщику
        products_list = Product.objects.filter(supplier__id=supplierlist[id].id)
        prod_txt = ""
       
        for product in products_list:
            prod_txt = prod_txt + product.prodName +": " + product.prodStatus + " " + product.statusData + """<div class="indent_br"></div>""" + "\n"



        tcenter = (tcenter
                   + "<tr><td>"
                   + str(supplierlist[id].id)
                   + "</td><td>"
                   + supplierlist[id].name
                   + "</td><td>"
                   + supplierlist[id].supplierinfo
                   + "</td><td>"
                   + supplierlist[id].cq
                   + "</td><td>"
                   + supplierlist[id].cqdata
                   + "</td><td>"
                   + str(prod_txt)
                   + "</td><td>"
                   + supplierlist[id].audited
                   + "</td></tr>"
                   + "\n")
        
    return HttpResponse(ttop + tcenter + tbottom)

# Станица вывода таблицы c данными по аттестации поставщиков End------------------------------------------------
# --------------------------------------------------------------------------------------------------------------





# Функция проверки даты и перевода в формат HTML 
def dateToHtml(datefirst):

    if datefirst == "":
        pqdatеstr = ""
        return pqdatеstr

    else:
        now = datetime.datetime.now()
        dateqalif = datetime.datetime.strptime(datefirst, "%Y-%m-%d")
            
        # Кол-во времени между текущей датой и датой аттестации.
        delta = now - dateqalif
        if delta.days > 1095:
            pqdatеstr = """<font color="FF1A1A">""" + "[" + str(dateqalif.strftime("%Y-%m-%d")) + "]" +"""</font>"""
        else:
            pqdatеstr = """<font color="00BC00">""" + "[" + str(dateqalif.strftime("%Y-%m-%d")) + "]" +"""</font>"""
            
        return pqdatеstr





# Функция проверки статуса и перевода в формат HTML 
def qStatusToHtml(status):

    if status == "Not qualified":
        return """<font color="FF1A1A">""" + status + """</font>"""
        
    elif status == "Qualified":
        return """<font color="#00BC00">""" + status + """</font>"""

    elif status == "Qualified with conditions":
        return """<font color="#DC9800">""" + status + """</font>"""
    
    else:
        return status
