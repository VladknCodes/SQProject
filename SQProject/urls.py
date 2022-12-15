from django.contrib import admin
from django.urls import path
from Supplier_Qualification import views
 
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main),
    path('main/', views.main),
    path('qualification_status/', views.qualification_status),
    path('audit_schedule/', views.audit_schedule),
    path('qprocess/', views.qprocess),
    path('dra/', views.dra),
    path('lqs/', views.lqs),

    path('viewdb/', views.viewdb),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    
    path('viewdbsp/', views.viewdbsp),
    path('createsp/', views.createsp),
    path('editsp/<int:id>/', views.editsp),
    path('deletesp/<int:id>/', views.deletesp),
    
    path('printdbsp/', views.printdbsp),
    
    path('viewdra/', views.viewdra),
    path('createdra/', views.createdra),
    path('editdra/<int:id>/', views.editdra),
    path('deletedra/<int:id>/', views.deletedra),

    path('qualification_status/<int:id>/', views.supplier),
    path('dra/<int:id>/', views.supplierdra),


        
]
