from django.contrib import admin
from django.urls import path
from Supplier_Qualification import views
 
urlpatterns = [
    
    # Административная панель
    path('admin/', admin.site.urls),

    
    # Основные страницы сайта
    path('', views.main),
    path('main/', views.main),
    path('qualification_status/', views.qualification_status),
    path('audit_schedule/', views.audit_schedule),
    path('qprocess/', views.qprocess),
    path('dra/', views.dra),
    path('lqs/', views.lqs),

    # Страницы просмотра и редактирования данных таблицы Person (данные по персоналу) 
    path('viewdb/', views.viewdb),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    
    # Страницы просмотра и редактирования данных таблицы Supplier (данные по аттестации поставщиков)
    path('viewdbsp/', views.viewdbsp),
    path('createsp/', views.createsp),
    path('editsp/<int:id>/', views.editsp),
    path('deletesp/<int:id>/', views.deletesp),
    
    # Станица вывода таблицы по аттестации поставщиков Start
    path('printdbsp/', views.printdbsp),
    
    # Страницы просмотра и редактирования данных таблицы DRA (данные по аудиту достоверности данных)
    path('viewdra/', views.viewdra),
    path('createdra/', views.createdra),
    path('editdra/<int:id>/', views.editdra),
    path('deletedra/<int:id>/', views.deletedra),

    # Страница поставщика по ID
    path('qualification_status/<int:id>/', views.supplier),
    
    # Cтраницы поставщика DRA по ID
    path('dra/<int:id>/', views.supplierdra),
        
]
