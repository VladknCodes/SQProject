# Supplier Qualification Portal.
# Developed by Kartashov Vladislav.
# 2023.

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Person
from .models import Supplier
from .models import DRA
from .models import News


import json
import datetime
import os



# Функции страниц сайта Start---------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

def main(request):
    news = News.objects.all()
    return render(request, "main.html", {'title' : "News", 'news' : news})

def qualification_status(request):
    splist = printtablelist ()
    return render(request, "qualification_status.html", {'title' : "Qualification status", 'splist' : splist})

def audit_schedule(request):
    return render(request, "audit_schedule.html", {'title' : "Audit schedule"})

def qprocess(request):
    return render(request, "qprocess.html", {'title' : "Qualification process"})

def dra(request):
    supplierlist = DRA.objects.all()
    return render(request, "dra.html", {'title' : "Data reliability audit", 'supplierlist' : supplierlist})

# Страница персонала
def lqs(request):
    people = Person.objects.all()

    # Создание словарей для  списка файлов и списка ссылок
    sert_lqs = {}
    link_files_dict = {}
    
    for per_id in people:

        # Формирование списка файлов - Certificates
        
        link_files = "/static/files/lqs/" + str(per_id.id) + "/"
        dirPath = "..\\static\\files\\lqs\\" + str(per_id.id)
        
        # Получение списка имен файлов в дереве каталога
        files = next(os.walk(dirPath))[2]

        # Добавление в словарь списка файлов и списка ссылок
        sert_lqs[per_id.id] = files
        link_files_dict [per_id.id] = link_files
        
          

    return render(request, "lqs.html", {
        'title' : "List of qualification specialists",
        'people' : people,
        'sert_lqs' : sert_lqs,
        'link_files_dict' : link_files_dict})




# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Функции страниц сайта End----------------------------------------------------------------------------------------------------------------------------------



# Загрузка страницы поставщика по ID--------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

def supplier(request, id):

    try:
        supplier = Supplier.objects.get(id=id)


        # Проверка на соответствие JSON
        try:
            pqjs = json.loads(supplier.pq)
        except ValueError as e:
            pqlist = ""
        else:
            pqlist = ""
            for t in pqjs:
                pqlist = pqlist + """<div>""" + t[0] +": " + t[1] + " " + t[2] + """</div>"""

        
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
            'pqlist' : pqlist,
            'filesCQ' : filesCQ,
            'filesPQ' : filesPQ,
            'link_files_cq' : link_files_cq,
            'link_files_pq' : link_files_pq})
            
    # При отсутвии в БД поставщика с данным запросом - Вывод информации на экран
    except Supplier.DoesNotExist:

        supplierContent = "Supplier not found"

        return render(request, "supplier_er.html", {'supplierContent' : supplierContent})



# Загрузка страницы поставщика - DRA по номеру заявки--------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

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











# Страница List of employees - Таблица Person (данные по персоналу) Start--------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Получение данных из БД
def viewdb(request):
    people = Person.objects.all()
    return render(request, "viewdb.html", {"people": people})
 
# Сохранение данных в БД
def create(request):
    if request.method == "POST":
        person = Person()
        
        person.lastName = request.POST.get("lastName")
        person.firstName = request.POST.get("firstName")
        person.position = request.POST.get("position")
        person.phone = request.POST.get("phone")
        person.email = request.POST.get("email")
        person.experience = request.POST.get("experience")
        person.description = request.POST.get("description")

        person.save()
    return HttpResponseRedirect("/viewdb")


# Изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.lastName = request.POST.get("lastName")
            person.firstName = request.POST.get("firstName")
            person.position = request.POST.get("position")
            person.phone = request.POST.get("phone")
            person.email = request.POST.get("email")
            person.experience = request.POST.get("experience")
            person.description = request.POST.get("description")

            person.save()
            return HttpResponseRedirect("/viewdb")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/viewdb")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# List of employees - Таблица Person End------------------------------------------------------------------------------------------------------------------------------------------





# Страница Supplier list - Таблица Supplier (данные по аттестации поставщиков) Start--------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Получение данных из БД
def viewdbsp(request):
    supplierlist = Supplier.objects.all()
    return render(request, "viewdbsp.html", {"supplierlist": supplierlist})
 
# Сохранение данных в БД
def createsp(request):
    if request.method == "POST":
        supplier = Supplier()
        supplier.name = request.POST.get("name")
        supplier.supplierinfo = request.POST.get("supplierinfo")
        supplier.cq = request.POST.get("cq")
        supplier.cqdata = request.POST.get("cqdata")
        supplier.pq = request.POST.get("pq")
        supplier.save()
    return HttpResponseRedirect("/viewdbsp")


# Изменение данных в БД
def editsp(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
 
        if request.method == "POST":
            supplier.name = request.POST.get("name")
            supplier.supplierinfo = request.POST.get("supplierinfo")
            supplier.cq = request.POST.get("cq")
            supplier.cqdata = request.POST.get("cqdata")
            supplier.pq = request.POST.get("pq")
            supplier.save()
            return HttpResponseRedirect("/viewdbsp")
        else:
            return render(request, "editsp.html", {"supplier": supplier})
    except Supplier.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")
     
# Удаление данных из БД
def deletesp(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
        supplier.delete()
        return HttpResponseRedirect("/viewdbsp")
    except Supplier.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Страница Supplier list - Таблица Supplier End----------------------------------------------------------------------------------------------------------------------------------------





# Страница DRA Supplier list - Таблица DRA (данные по аудиту достоверности данных) Start--------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Получение данных из БД-DRA
def viewdra(request):
    supplierlist = DRA.objects.all()
    return render(request, "viewdra.html", {"supplierlist": supplierlist})
 
# Сохранение данных в БД-DRA
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

        supplier.save()
    return HttpResponseRedirect("/viewdra")


# Изменение данных в БД-DRA
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
            
            supplier.save()
            return HttpResponseRedirect("/viewdra")
        else:
            return render(request, "editdra.html", {"supplier": supplier})
    except DRA.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")
     
# Удаление данных из БД-DRA
def deletedra(request, id):
    try:
        supplier = DRA.objects.get(id=id)
        supplier.delete()
        return HttpResponseRedirect("/viewdra")
    except DRA.DoesNotExist:
        return HttpResponseNotFound("<h2>Supplier not found</h2>")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Страница DRA Supplier list - Таблица DRA End----------------------------------------------------------------------------------------------------------------------------------------





# Станица вывода таблицы по аттестации поставщиков Start--------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------


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
    </tr>
    """
    tcenter = ""

    tbottom ="""
    </tbody>
    </table>
    """
        
    for id in supplierlist:

        # Проверка на соответствие JSON
        try:
            pqjs = json.loads(supplierlist[id].pq)
        except ValueError as e:
            pqlist = ""
        else:
            pqlist = ""
            for t in pqjs:
                pqlist = pqlist + t[0] +": " + t[1] + " " + t[2] + """<div class="indent_br"></div>""" + "\n"


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
                   + str(pqlist)
                   + "</td></tr>"
                   + "\n")
        
        
    return HttpResponse(ttop + tcenter + tbottom)

# Станица вывода таблицы по аттестации поставщиков End--------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------







# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Дополнительные функции для работы сайта-----------------------------------------------------------------------------------------------------------------



# Функция вывода списка по аттестации поставщиков на странице сайта "qualification_status"
def printtablelist ():
    
    
    supplierlist = Supplier.objects.in_bulk()
    ttop = """
    <table class="table_st">
        <thead class="table_thead_st">
            <tr class="table_tr_st">
                <th class="table_th_td_st">#</th>
                <th class="table_th_td_st">Supplier</th>
                <th class="table_th_td_st">Commercial qualification</th>
                <th class="table_th_td_st">Product qualification</th>
            </tr>
        </thead>
    <tbody>
    """
    tcenter = ""

    tbottom ="""
    </tbody>
    </table>
    """
        
    for id in supplierlist:

        # Проверка на соответствие JSON
        try:
            pqjs = json.loads(supplierlist[id].pq)
        except ValueError as e:
            pqlist = ""
        else:
            pqlist = ""
            for t in pqjs:
                pqlist = pqlist + t[0] +": " + qStatusToHtml(t[1]) + " " + dateToHtml(t[2]) + "<br>"



        tcenter = (tcenter
                   + """<tr class="table_tr_st table_tr_link"><th class="table_th_td_st">"""
                   + str(supplierlist[id].id)
                   + """</th><td class="table_th_td_st bold">"""
                   + """<a class="main_link_tr" href='/qualification_status/"""
                   + str(supplierlist[id].id)
                   + """/'>"""
                   + supplierlist[id].name
                   +"""</a>"""
                   + """</td><td class="table_th_td_st">"""
                   + qStatusToHtml(supplierlist[id].cq)
                   + " "
                   + dateToHtml(supplierlist[id].cqdata)
                   + """</td><td class="table_th_td_st">"""
                   + str(pqlist)
                   + "</td></tr>"
                   + "\n")
       
        statustable = ttop + tcenter + tbottom

    return statustable





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
 
