from django.forms import ModelForm
from .models import Registro
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class registrofirst(ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha', 'detalles', 'efectivosaldo', 'bancosaldo']
        widgets = {'fecha': DateInput()}
    def __init__(self, *args, **kwargs):
        super(registrofirst, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['class'] = 'form-control'
        self.fields['fecha'].widget.attrs['placeholder'] = 'Ingrese la fecha del registro'
        self.fields['detalles'].widget.attrs['class'] = 'form-control'
        self.fields['detalles'].widget.attrs['placeholder'] = 'Ingrese el detalle del registro'
        self.fields['efectivosaldo'].widget.attrs['class'] = 'form-control'
        self.fields['efectivosaldo'].widget.attrs['placeholder'] = 'Ingrese el saldo inicial en efectivo'
        self.fields['bancosaldo'].widget.attrs['class'] = 'form-control'
        self.fields['bancosaldo'].widget.attrs['placeholder'] = 'Ingrese el saldo inicial en banco'

class seleccionR(ModelForm):
    class Meta:
        model = Registro
        fields = ['tipodeseleccion']
    def __init__(self, *args, **kwargs):
        super(seleccionR, self).__init__(*args, **kwargs)
        self.fields['tipodeseleccion'].widget.attrs['class'] = 'form-control'

class registroEfectivo(ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha','detalles','numerocomprobante','efectivoingresos', 'efectivoegresos']
        widgets = {'fecha': DateInput()}
    def __init__(self, *args, **kwargs):
        super(registroEfectivo, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['class'] = 'form-control'
        self.fields['fecha'].widget.attrs['placeholder'] = 'Ingrese la fecha del registro'
        self.fields['detalles'].widget.attrs['class'] = 'form-control'
        self.fields['detalles'].widget.attrs['placeholder'] = 'Ingrese el detalle del registro'
        self.fields['numerocomprobante'].widget.attrs['class'] = 'form-control'
        self.fields['numerocomprobante'].widget.attrs['placeholder'] = 'Ingrese el número de comprobante'
        self.fields['numerocomprobante'].label = 'Número de comprobante'
        self.fields['efectivoingresos'].widget.attrs['class'] = 'form-control'
        self.fields['efectivoegresos'].widget.attrs['class'] = 'form-control'
        self.fields['efectivoingresos'].widget.attrs['placeholder'] = 'Ingrese los ingresos del registro'
        self.fields['efectivoingresos'].label = 'Ingresos'
        self.fields['efectivoegresos'].widget.attrs['placeholder'] = 'Ingrese los egresos del registro' 
        self.fields['efectivoegresos'].label = 'Egresos'

class registroBanco(ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha','detalles','numerocomprobante','bancoingresos', 'bancoegresos']
        widgets = {'fecha': DateInput()}
    def __init__(self, *args, **kwargs):
        super(registroBanco, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['class'] = 'form-control'
        self.fields['fecha'].widget.attrs['placeholder'] = 'Ingrese la fecha del registro'
        self.fields['detalles'].widget.attrs['class'] = 'form-control'
        self.fields['detalles'].widget.attrs['placeholder'] = 'Ingrese el detalle del registro'
        self.fields['numerocomprobante'].widget.attrs['class'] = 'form-control'
        self.fields['numerocomprobante'].widget.attrs['placeholder'] = 'Ingrese el número de comprobante'
        self.fields['numerocomprobante'].label = 'Número de comprobante'
        self.fields['bancoingresos'].widget.attrs['class'] = 'form-control'
        self.fields['bancoegresos'].widget.attrs['class'] = 'form-control'
        self.fields['bancoingresos'].widget.attrs['placeholder'] = 'Ingrese los ingresos del registro'
        self.fields['bancoingresos'].label = 'Ingresos'
        self.fields['bancoegresos'].widget.attrs['placeholder'] = 'Ingrese los egresos del registro' 
        self.fields['bancoegresos'].label = 'Egresos'