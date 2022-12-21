from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Social(models.Model):
    mediasocial=(
        ('tiktok','tiktok'),
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('twitter','twitter'),
        ('whatsapp','whatsapp'),
        ('linkedin','linkedin'),
        ('twitch','twitch'),
        ('pinterest','pinterest'),
        ('messenger','messenger'),
    )
    Icono = models.CharField(max_length=150,choices=mediasocial, verbose_name='Icono')
    SocialMedia = models.URLField(max_length=200, verbose_name='Direccion')

    def __str__(self):
        return self.Icono

    class Meta:
        db_table = 'social'
        managed = True
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

class Presentacion(models.Model):
    Nombre = models.CharField(max_length=150, verbose_name='Nombre')
    Profesiones = models.CharField(max_length=150, verbose_name='Profesiones')
    PortadaFondo = models.ImageField(upload_to='static/img/front', height_field=None, width_field=None, max_length=100)
    SocialM = models.ManyToManyField(Social)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'presentacion'
        managed = True
        verbose_name = 'Presentacion'
        verbose_name_plural = 'Presentaciones'

class AcercaDe(models.Model):
    FotoPerfil = models.ImageField(upload_to='static/img/front', height_field=None, width_field=None, max_length=100, verbose_name='Foto de Perfil')
    AcercaDe = models.TextField(help_text='Coloque algo acerca de Usted', verbose_name='Acerca de ti')
    Puesto = models.CharField(max_length = 150, verbose_name='Perfil del Puesto')
    Cumpleaños = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Nacimiento')
    Edad = models.PositiveSmallIntegerField(verbose_name='Edad')
    Direccion = models.CharField(max_length = 250, verbose_name='Direccion')
    Mail = models.CharField(max_length = 250, verbose_name='E-Mail')
    Telefono = models.CharField(max_length = 50, verbose_name='Telefono')
    Proposito = models.TextField(help_text='Describa un logro a futuro', verbose_name='Metas',blank=True, null=True,)
    Proposito2 = models.TextField(help_text='Describa el proposito por el cual busca empleo', verbose_name='Proposito',blank=True, null=True,)
    Ubicacion = models.TextField(max_length = 1400, help_text='Coloque una Ubicaicon de su Domicilio, debe de ser aproximada. Nunca debe de colocar una ubicacion Excata, en formato iframe', verbose_name='Unicación',blank=True, null=True,)
    
    

    def __str__(self):
        return self.Puesto

    class Meta:
        db_table = 'acerca'
        managed = True
        verbose_name = 'Acerca'
        verbose_name_plural = 'Acerca de'

class Software(models.Model):
    Enfoque = models.TextField(help_text='Una introduccion de sus enfoque de habilidades en Software', verbose_name='Software a usar', blank=True, null=True,)
    Software = models.CharField(max_length = 150, verbose_name='Software')
    Porcentaje = models.PositiveSmallIntegerField(verbose_name='Aprovechamiento')
    
    def __str__(self):
        return self.Software

    class Meta:
        db_table = 'conocimiento'
        managed = True
        verbose_name = 'Conocimiento'
        verbose_name_plural = 'Conocimientos'

class Lenguajes(models.Model):
    Descripcion = models.TextField(help_text='Una introduccion de los conocimientos de su lenguaje de programacion', verbose_name='Introduccion de Lenguajes', blank=True, null=True,)
    lenguaje = models.CharField(max_length = 150, verbose_name='Lenguaje')
    Porcentaje = models.PositiveSmallIntegerField(verbose_name='Aprovechamiento')
    
    def __str__(self):
        return self.lenguaje

    class Meta:
        db_table = 'lenguaje'
        managed = True
        verbose_name = 'Lenguaje'
        verbose_name_plural = 'Lenguajes'

class Experiencia(models.Model):
    Introduccion = models.TextField(help_text='Una introduccion de las experiencias laborales', verbose_name='experiencia laboral', blank=True, null=True,)
    Empresa = models.CharField(max_length = 150, verbose_name='Empresa')
    Puesto = models.CharField(max_length = 150, verbose_name='Puesto')
    FechaInicio = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de inicio')
    FechaFin = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de fin', blank=True, null=True,)
    Salario = models.PositiveIntegerField(verbose_name='Salario', blank=True, null=True,)

    def __str__(self):
        return '{}-{}'.format(self.Empresa, self.Puesto)

    class Meta:
        db_table = 'experiencia'
        managed = True
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

class Portafolio(models.Model):
    Foto = models.ImageField(upload_to='static/img/portafolio', height_field=None, width_field=None, max_length=100)
    Etiqueta = models.CharField(max_length = 150, verbose_name='Etiqueta')
    Descripcion = models.TextField(help_text='Introduzca una descripcion', verbose_name='Descripcion', blank=True, null=True,)

    def __str__(self):
        return self.Etiqueta

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'

class Contacto(models.Model):
    Nombre = models.CharField(max_length = 150, verbose_name='Nombre')
    Empresa = models.CharField(max_length = 150, verbose_name='Empresa')
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario Asignado')
    Telefono = models.CharField(max_length = 150, verbose_name='Telefono')
    Correo = models.CharField(max_length = 150, verbose_name='Correo')
    Mensaje = models.TextField(help_text='Introduzca una su mensaje', verbose_name='Mensaje')
    completado = models.BooleanField(default=False, verbose_name='Acepto enviar mis datos para futuro contacto')

    def __str__(self):
        return '{}-{}'.format(self.Nombre, self.Empresa)

    class Meta:
        db_table = 'contacto'
        managed = True
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'