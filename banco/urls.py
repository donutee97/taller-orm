from django.urls import path, include
from . import views 

urlpatterns = [
    path('cuentas/', views.listar_cuentas, name='listar_cuentas'),
    path('registrar/', views.registrar_cuenta, name='registrar_cuenta'),
    path('actualizar/<int:id>/', views.actualizar_cuenta, name='actualizar_cuenta'),
    path('eliminar/<int:id>/', views.eliminar_cuenta, name='eliminar_cuenta'),
]