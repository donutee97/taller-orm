from django.db import models

# Create your models here.
class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_cuenta = models.IntegerField() # O charField(max_length=50) si deseas almacenar el tipo de cuenta como texto
    descripcion = models.CharField(max_length=255)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'cuenta'

    def __str__(self):
        return f"{self.descripcion} - {self.saldo}"