from django.contrib import admin
from .models import Curso
# Register your models here.

class Filtro_creditos(admin.ModelAdmin):
    list_filter=('creditos',)
    

admin.site.register(Curso, Filtro_creditos)