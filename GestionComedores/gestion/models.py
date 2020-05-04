from django.contrib.auth.models import User
from django.db import models
import datetime


class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"


class Escuela(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, related_name='secciones')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, help_text='Número de escuela', null=True, blank=True)
    latitud = models.FloatField(null=True, editable=False)
    longitud = models.FloatField(null=True, editable=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"


class Vinculo(models.TextChoices):
    PADRE = 'Padre', 'Padre'
    MADRE = 'Madre', 'Madre'
    OTRO = 'Otro', 'Otro'


class TipoDocumento(models.TextChoices):
    DNI = 'DNI', 'DNI'
    LC = 'LC', 'LC'
    LE = 'LE', 'LE'
    PASAPORTE = 'PASAPORTE', 'PASAPORTE'
    OTRO = 'OTRO', 'OTRO'


class Sexo(models.TextChoices):
    MASCULINO = 'Masculino', 'masculino'
    FEMENINO = 'Femenino', 'femenino'
    OTRO = 'Otro', 'otro'


class Solicitante(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='escuela_solicitante')
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(
        max_length=50,
        null=True,
        default=TipoDocumento.DNI,
        choices=TipoDocumento.choices,
    )
    numero_documento = models.CharField(max_length=30, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(
        max_length=20,
        choices=Sexo.choices,
        default=Sexo.MASCULINO,
    )
    grado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    vinculo = models.CharField(
        max_length=50,
        null=True,
        choices=Vinculo.choices,
    )
    apellido_reponsable = models.CharField(max_length=100)
    nombre_reponsable = models.CharField(max_length=100)
    tipo_documento_reponsable = models.CharField(
        max_length=20,
        default=TipoDocumento.DNI,
        choices=TipoDocumento.choices,
    )
    numero_documento_reponsable = models.CharField(max_length=30, null=True, blank=True)
    sexo_responsable = models.CharField(
        max_length=20,
        choices=Sexo.choices,
        default=Sexo.MASCULINO,
    )
    grupo_familiar = models.IntegerField(default=1)
    activo = models.BooleanField(default=True)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.apellido + ', ' + self.nombre


class Necesidad(models.Model):
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return self.descripcion


class NecesidadSolicitante(models.Model):
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE, related_name='sol_necesidad')
    necesidad = models.ForeignKey(Necesidad, on_delete=models.CASCADE, related_name='nec_solicitante')
    cubierta = models.BooleanField(default=False)
    fecha_solicitud = models.DateField(default=datetime.date.today)
    fecha_cobertura = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.necesidad.descripcion
