from django import forms
from .models import Cliente, Equipo, Tecnico, Reparacion


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "telefono", "email", "direccion"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            "cliente",
            "tipo",
            "marca",
            "modelo",
            "numero_serie",
            "observaciones",
        ]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "numero_serie": forms.TextInput(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
        }
class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = [
            "nombre",
            "apellido",
            "telefono",
            "especialidad",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "especialidad": forms.TextInput(attrs={"class": "form-control"}),
        }
class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = [
            "equipo",
            "tecnico",
            "fecha_ingreso",
            "fecha_entrega",
            "problema_reportado",
            "diagnostico",
            "solucion",
            "costo",
            "estado",
        ]
        widgets = {
            "equipo": forms.Select(attrs={"class": "form-control"}),
            "tecnico": forms.Select(attrs={"class": "form-control"}),
            "fecha_ingreso": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_entrega": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "problema_reportado": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "diagnostico": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "solucion": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "costo": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "estado": forms.Select(attrs={"class": "form-control"}),
        }
        
class ClientesFilter(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']


class EquipoFilter(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['cliente', 'tipo', 'marca', 'modelo', 'numero_serie', 'observaciones']
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "numero_serie": forms.TextInput(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class TecnicoFilter(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'apellido', 'telefono', 'especialidad']
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "especialidad": forms.TextInput(attrs={"class": "form-control"}),
        }


class ReparacionFilter(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = ['equipo', 'tecnico', 'fecha_ingreso', 'fecha_entrega', 'problema_reportado', 'diagnostico', 'solucion', 'costo', 'estado']
        widgets = {
            "equipo": forms.Select(attrs={"class": "form-control"}),
            "tecnico": forms.Select(attrs={"class": "form-control"}),
            "fecha_ingreso": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "fecha_entrega": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "problema_reportado": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "diagnostico": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "solucion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "costo": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "estado": forms.Select(attrs={"class": "form-control"}),
        }
        