# Portfolio Profesional - Django

Sitio web profesional desarrollado con Django que funciona como escaparate profesional, portfolio o curriculum digital.

## Inicio
<img width="1915" height="447" alt="Captura de pantalla 2025-11-02 161856" src="https://github.com/user-attachments/assets/74594347-cb40-4e63-b25e-886d73c69a70" />

## Trabajos
<img width="1919" height="524" alt="Captura de pantalla 2025-11-02 161929" src="https://github.com/user-attachments/assets/027b0a8c-704c-4bd7-8896-28407678d01b" />

## Curriculum
<img width="1899" height="871" alt="Captura de pantalla 2025-11-02 162038" src="https://github.com/user-attachments/assets/30a203bf-4f84-4821-ac2a-409364a64789" />

## Tecnologías
<img width="1908" height="856" alt="Captura de pantalla 2025-11-02 162100" src="https://github.com/user-attachments/assets/814c7b68-0b11-4f1a-a4aa-bf599f204cc8" />

## Acerca de mí
<img width="1908" height="856" alt="Captura de pantalla 2025-11-02 162100" src="https://github.com/user-attachments/assets/88a7a82e-988b-4443-98db-ca0233154045" />

## Contacto
<img width="1919" height="804" alt="Captura de pantalla 2025-11-02 162017" src="https://github.com/user-attachments/assets/91119a2c-781d-41c3-8b96-c824b5b98713" />





## Características

- **Página de Inicio**: Visión general del perfil con trabajos destacados
- **Trabajos Realizados**: Galería de proyectos profesionales y personales
- **Acerca de Mí**: Biografía, habilidades y objetivos profesionales
- **Contacto**: Formulario de contacto funcional con envío de emails

## Requisitos

- Python 3.8 o superior
- Django 4.2
- Pillow (para manejo de imágenes)

## Instalación

1. Clonar o descargar el proyecto

2. Crear un entorno virtual:
```bash
python -m venv venv
```

3. Activar el entorno virtual:
   - En Windows:
   ```bash
   venv\Scripts\activate
   ```
   - En Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

5. Ejecutar las migraciones:
```bash
python manage.py migrate
```

6. Crear un superusuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

8. Acceder al sitio web:
   - Sitio principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Configuración del Contenido

### 1. Crear Perfil

Ve al panel de administración (`/admin/`) y crea un registro en **Portfolio > Perfils** con:
- Nombre completo
- Título profesional
- Biografía
- Email de contacto
- Foto personal (opcional)
- Enlaces a redes sociales (opcional)

### 2. Agregar Habilidades

En **Portfolio > Habilidades**, agrega tus habilidades técnicas y profesionales:
- Nombre de la habilidad
- Categoría (Frontend, Backend, Diseño, etc.)
- Nivel (Básico, Intermedio, Avanzado, Experto)
- Descripción (opcional)

### 3. Agregar Trabajos/Proyectos

En **Portfolio > Trabajos**, agrega tus proyectos:
- Título del proyecto
- Descripción
- Tipo (Profesional, Personal, Académico)
- Imagen (opcional)
- URLs del proyecto y repositorio (opcional)
- Tecnologías utilizadas (separadas por comas)
- Marcar como destacado para que aparezca en la página de inicio

### 4. Configurar Email (Opcional para Producción)

Para que el formulario de contacto envíe emails reales, edita `portfolio_project/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-password'
DEFAULT_FROM_EMAIL = 'tu-email@gmail.com'
```

## Estructura del Proyecto

```
portfolio_project/
├── manage.py
├── requirements.txt
├── portfolio_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── portfolio/
    ├── models.py          # Modelos de datos
    ├── views.py           # Vistas de las páginas
    ├── forms.py           # Formularios
    ├── admin.py           # Configuración del admin
    └── templates/
        └── portfolio/     # Templates HTML
```

## Personalización

- **Colores**: Edita las variables CSS en `templates/portfolio/base.html` (líneas de `:root`)
- **Estilos**: Modifica los estilos en el mismo archivo base.html
- **Contenido**: Todo el contenido se gestiona desde el panel de administración

## Notas de Seguridad

⚠️ **Importante para producción:**
- Cambiar `SECRET_KEY` en `settings.py`
- Cambiar `DEBUG = False`
- Configurar `ALLOWED_HOSTS`
- Usar una base de datos más robusta (PostgreSQL, MySQL)
- Configurar archivos estáticos correctamente

## Licencia

Este proyecto está disponible para uso personal y profesional.

