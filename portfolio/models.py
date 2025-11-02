from django.db import models
from django.core.validators import URLValidator


class Perfil(models.Model):
    nombre = models.CharField(max_length=100, default="Antonio Lorenzo")
    titulo = models.CharField(max_length=200, help_text="Ej: Desarrollador Full Stack, Diseñador UX/UI")
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True)
    biografia = models.TextField(help_text="Tu historia profesional")
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    ubicacion = models.CharField(max_length=100, blank=True)
    
    linkedin = models.URLField(blank=True, validators=[URLValidator()])
    github = models.URLField(blank=True, validators=[URLValidator()])
    twitter = models.URLField(blank=True, validators=[URLValidator()])
    instagram = models.URLField(blank=True, validators=[URLValidator()])
    
    objetivos = models.TextField(blank=True, help_text="Tus objetivos profesionales")
    
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Perfil"
        ordering = ['-fecha_actualizacion']
    
    def __str__(self):
        return self.nombre


class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
        ('experto', 'Experto'),
    ]
    
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, help_text="Ej: Frontend, Backend, Diseño")
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='intermedio')
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='tecnologias/', blank=True, null=True, help_text="Logo/icono de la tecnología (recomendado: 64x64px)")
    mostrar_en_circulo = models.BooleanField(default=False, help_text="Mostrar en la sección de tecnologías con animación circular")
    orden = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        verbose_name_plural = "Habilidades"
        ordering = ['categoria', 'orden', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"


class Curriculum(models.Model):
    TIPO_CHOICES = [
        ('trabajo', 'Experiencia Laboral'),
        ('educacion', 'Educación'),
        ('certificacion', 'Certificación'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='trabajo')
    titulo = models.CharField(max_length=200)
    empresa_institucion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(help_text="Descripción de las responsabilidades o logros")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True, help_text="Dejar vacío si es actual")
    es_actual = models.BooleanField(default=False, help_text="Marcar si es la posición/estudio actual")
    orden = models.IntegerField(default=0, help_text="Orden de visualización (mayor = más reciente)")
    
    class Meta:
        verbose_name_plural = "Currículum"
        ordering = ['-orden', '-fecha_inicio']
    
    def __str__(self):
        return f"{self.titulo} - {self.empresa_institucion}"


class Trabajo(models.Model):
    TIPO_CHOICES = [
        ('profesional', 'Profesional'),
        ('personal', 'Personal'),
        ('academico', 'Académico'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='profesional')
    imagen = models.ImageField(upload_to='trabajos/', blank=True, null=True)
    url_proyecto = models.URLField(blank=True, validators=[URLValidator()])
    url_repositorio = models.URLField(blank=True, validators=[URLValidator()])
    tecnologias = models.CharField(max_length=500, help_text="Tecnologías usadas, separadas por comas")
    fecha_realizacion = models.DateField(blank=True, null=True)
    destacado = models.BooleanField(default=False, help_text="Mostrar en la página de inicio")
    orden = models.IntegerField(default=0, help_text="Orden de visualización")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Trabajos"
        ordering = ['-destacado', 'orden', '-fecha_realizacion']
    
    def __str__(self):
        return self.titulo
    
    def tecnologias_lista(self):
        return [tech.strip() for tech in self.tecnologias.split(',') if tech.strip()]


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.nombre} - {self.asunto}"

