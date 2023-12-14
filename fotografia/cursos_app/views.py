from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Cursos

# Create your views here.


class CursosBaseView(View):
    template_name = 'cursos.html'
    model = Cursos
    fields = '__all__'
    success_url = reverse_lazy('cursos:all')


class CursosListView(CursosBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS Cursos
    """

class CursosDetailView(CursosBaseView,DetailView):
    template_name = "curso_detail.html"

class CursosCreateView(CursosBaseView,CreateView):
    template_name = "curso_create.html"
    extra_context = {
        "tipo": "Crear curso"
    }


class CursosUpdateView(CursosBaseView,UpdateView):
    template_name = "curso_create.html"
    extra_context = {
        "tipo": "Actualizar curso"
    }

class CursosDeleteView(CursosBaseView,DeleteView):
    template_name = "curso_delete.html"
    extra_context = {
        "tipo": "Borrar curso"
    }


