from django import forms
from agenda.models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellidos', 'telefono', 'email', 'direccion', 'localidad']
        
        