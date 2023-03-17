from django.contrib import admin

from .models import Person, Supplier, DRA, News, Product, DRAauditors

admin.site.register(Person)
admin.site.register(Supplier)
admin.site.register(DRA)
admin.site.register(News)
admin.site.register(Product)
admin.site.register(DRAauditors)
