from django.db import models
 
# Класс для таблицы с данными по персоналу
class Person(models.Model):
    lastName = models.CharField(max_length=50, null=True, blank=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

# Класс для таблицы с данными по аттестации поставщиков
class Supplier(models.Model):
    name = models.TextField(null=True, blank=True)
    supplierinfo = models.TextField(null=True, blank=True)
    cq = models.TextField(null=True, blank=True)
    cqdata = models.TextField(null=True, blank=True)
    pq = models.TextField(null=True, blank=True)
    audited = models.TextField(null=True, blank=True)

# Класс для таблицы с данными аудиту достоверности данных
class DRA(models.Model):
    numberItem = models.IntegerField(null=False, blank=True)
    numberOrd = models.IntegerField(null=False, blank=True)
    dateOrd = models.CharField(max_length=20, null=False, blank=True)
    supplier = models.TextField(null=False, blank=True)
    supplierinfo = models.TextField(null=False, blank=True)
    procedureProc = models.CharField(max_length=50, null=False, blank=True)
    purchasedProd = models.TextField(null=False, blank=True)
    dateAudit = models.CharField(max_length=20, null=False, blank=True)
    auditResult = models.CharField(max_length=10, null=False, blank=True)
    numberAudit = models.CharField(max_length=10, null=False, blank=True)
    comment = models.TextField(null=False, blank=True)
    auditors = models.TextField(null=True, blank=True)

# Класс для таблицы с данными по новостному блоку
class News(models.Model):
    dateNews = models.CharField(max_length=20, null=True, blank=True)
    dataNews = models.TextField(null=True, blank=True)
