from django.db import models
from django.db.models import Model

# Create your models here.
class Cursos(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    
    nombre = models.CharField(max_length=100, default="Alumno x")
    duracion = models.CharField(max_length=100, default="Meses x", blank=False, null=False)
    contacto = models.EmailField(max_length=100, default="no_contact@mail.com")
    horario = models.CharField(max_length=100, default="Horario x")
    fecha_comienzo = models.DateField(blank=False, null=False, auto_now=True)

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    class Meta:
       db_table = "cursos_fotografia"


    def __str__(self):
        return f"El nombre del curso: {self.nombre}, dura: {self.duracion}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]


