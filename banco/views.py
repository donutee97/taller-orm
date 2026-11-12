from django.shortcuts import render, redirect
from .models import Cuenta  # Importamos tu modelo

# Create your views here.

def listar_cuentas(request):
    # Esto equivale a un: SELECT * FROM cuenta;
    cuentas = Cuenta.objects.all() 
    
    # Enviamos los datos al HTML mediante el diccionario de contexto
    return render(request, 'gestionCuentas.html', {'cuentas': cuentas})

# VISTA 2: Solo se encarga de insertar (INSERT)
def registrar_cuenta(request):
    if request.method == 'POST':
        v_tipocuenta = request.POST.get('txtTipoCuenta')
        v_descripcion = request.POST.get('txtDescripcion')
        v_saldo = request.POST.get('txtSaldo')
        
        Cuenta.objects.create(
            tipo_cuenta=v_tipocuenta,
            descripcion=v_descripcion,
            saldo=v_saldo
        )
    # Al terminar de insertar, redirige a la vista de consultas para actualizar la tabla
    return redirect('listar_cuentas')

def actualizar_cuenta(request, id):
    # Obtenemos la cuenta por su ID
    cuenta = Cuenta.objects.get(id=id)
    
    if request.method == 'POST':
        # Actualizamos los campos de la cuenta
        cuenta.tipo_cuenta = request.POST.get('txtTipoCuenta')
        cuenta.descripcion = request.POST.get('txtDescripcion')
        cuenta.saldo = request.POST.get('txtSaldo')
        cuenta.save()  # Guardamos los cambios en la base de datos
        
        # Redirigimos a la vista de listar cuentas para actualizar la tabla
        return redirect('listar_cuentas')
    
    # Si no es un POST, renderizamos el formulario con los datos actuales de la cuenta
    return render(request, 'actualizarCuenta.html', {'cuenta': cuenta})

def eliminar_cuenta(request, id):
    # Obtenemos la cuenta por su ID
    cuenta = Cuenta.objects.get(id=id)
    
    # Eliminamos la cuenta
    cuenta.delete()
    
    # Redirigimos a la vista de listar cuentas para actualizar la tabla
    return redirect('listar_cuentas')

# Create your views here.
