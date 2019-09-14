from django.db import models
from tenant_schemas.models import TenantMixin

# Create your models here.
class Empresa(TenantMixin):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True, help_text='Página web de su empresa.')


    auto_create_schemas = True

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre