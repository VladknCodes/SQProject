from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse


from django.contrib.auth.decorators import login_required

from Supplier_Qualification.models import Person



# Страница администрирования базы данных
# --------------------------------------------------------------------------------------------------------------
# Страница List of employees - Таблица Person (данные по персоналу) Start---------------------------------------
# --------------------------------------------------------------------------------------------------------------

# Получение данных из БД
@login_required
def viewdb(request):
    people = Person.objects.all()
    return render(request, "viewdb.html", {"people": people})


# Сохранение данных в БД
@login_required
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
@login_required
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
@login_required
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/viewdb")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# --------------------------------------------------------------------------------------------------------------
# List of employees - Таблица Person End------------------------------------------------------------------------
