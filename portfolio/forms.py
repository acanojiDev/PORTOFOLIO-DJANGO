from django import forms
from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com',
                'required': True
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto del mensaje',
                'required': True
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 5,
                'required': True
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }

