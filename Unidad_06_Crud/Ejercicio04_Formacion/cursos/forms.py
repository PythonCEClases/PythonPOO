from django import forms
from cursos.models import Curso, Estudiante


class NuevoEstudianteForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(label="Selecciona cursos", 
            queryset=Curso.objects.all(), widget=forms.SelectMultiple)
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'cursos': forms.SelectMultiple(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }
        
    def __init__(self, *args, **kwargs):
        super(NuevoEstudianteForm, self).__init__(*args, **kwargs)
        self.fields['cursos'].queryset = Curso.objects.all()
