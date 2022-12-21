from django.forms import *
from cv.models import *

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ('Nombre', 'Empresa', 'Usuario', 'Telefono', 'Correo', 'Mensaje', 'completado')
        widgets = {
            'Nombre': TextInput(attrs={'class':'form-control', }),
            'Empresa': TextInput(attrs={'class':'form-control', }),
            'Mensaje': Textarea(attrs={'cols': 35, 'rows': 20, 'class':'form-control'}),
            'Telefono': TextInput(attrs={'class':'form-control', }),
            'Usuario': Select(attrs={'class':'form-control'},),
            'Correo' : EmailInput(attrs= {'placeholder':'Email','class':'form-control'}),
            'completado' : CheckboxInput(attrs={'class':'form-check',}),
        }