from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Cursos

# Register your models here.

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    ...