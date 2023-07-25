from django.shortcuts import render

from Supplier_Qualification.models import Person

import os


# Функция вывода информации по специалистам для страницы List of qualification specialists----------------------
# --------------------------------------------------------------------------------------------------------------


def lqs(request):
    people = Person.objects.all()

    # Создание словарей для списка файлов и списка ссылок
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
