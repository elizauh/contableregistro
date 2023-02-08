from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
def valid(value):
    if value < 0.0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class Registro(models.Model):
    fecha = models.DateField()
    detalles = models.CharField(max_length=200)
    numerocomprobante = models.CharField(max_length=200)
    TIPO = (
        ('E', 'Efectivo'),
        ('B', 'Banco'),
    )
    tipodeseleccion = models.CharField(max_length=200, choices=TIPO, blank=True, null=True)
    efectivoingresos = models.FloatField(validators=[valid], blank=True, null=True)
    efectivoegresos = models.FloatField(validators=[valid], blank=True, null=True)
    efectivosaldo = models.FloatField(validators=[valid], blank=True, null=True)
    bancoingresos = models.FloatField(validators=[valid], blank=True, null=True)
    bancoegresos = models.FloatField(validators=[valid], blank=True, null=True)
    bancosaldo = models.FloatField(validators=[valid], blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.detalle