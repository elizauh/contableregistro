from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate
from django.db import IntegrityError
from .forms import registrofirst, seleccionR, registroEfectivo, registroBanco
from .models import Registro

def base(request):
    if request.user.is_authenticated:
        datoregistros = Registro.objects.filter(user=request.user)
        tamanio = len(datoregistros)
        print(tamanio)
        return render(request, 'home.html', {'tamanio': tamanio})
    else:
        return render(request, 'home.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                auth_login(request, user)
                return redirect('principalusuarios')
            except IntegrityError:
                return render(request, 'registro.html', {'form': UserCreationForm(), 'error': 'El usuario ya existe'})
        return render(request, 'registro.html', {'form': UserCreationForm(), 'error': 'Las contraseñas no coinciden'})

def principalusuarios(request):
    datoregistros = Registro.objects.filter(user=request.user)
    tamanio = len(datoregistros)
    return render(request, 'principalusuarios.html', {'datoregistros': datoregistros, 'tamanio': tamanio})

def crearSaldos(request):
    datoregistros = Registro.objects.filter(user=request.user)
    tamanio = len(datoregistros)
    if request.method == 'GET':
        return render(request, 'primerRegistro.html', {'form': registrofirst()})
    else:
        try:
            form = registrofirst(request.POST)
            nuevoRegistro = form.save(commit=False)
            if nuevoRegistro.efectivoingresos is None:
                nuevoRegistro.efectivoingresos = 0.0
            if nuevoRegistro.efectivoegresos is None:
                nuevoRegistro.efectivoegresos = 0.0
            if nuevoRegistro.bancoingresos is None:
                nuevoRegistro.bancoingresos = 0.0
            if nuevoRegistro.bancoegresos is None:
                nuevoRegistro.bancoegresos = 0.0
            nuevoRegistro.user = request.user
            nuevoRegistro.save()

            return redirect('principalusuarios')
        except ValueError:
            return render(request, 'primerRegistro.html', {'form': registrofirst(),  'error': 'Datos incorrectos', 'tamanio': tamanio})

def seleccionTipo(request):
    datoregistros = Registro.objects.filter(user=request.user)
    tamanio = len(datoregistros)
    if request.method == 'GET':
        return render(request, 'seleccionartipo.html', {'form': seleccionR(), 'tamanio': tamanio})
    else:
        if request.POST['tipodeseleccion'] == 'E':
            return redirect('crearRegistroEfectivo')
        else:
            return redirect('crearRegistroBanco')
        

def crearREfectivo(request):
    datoregistros = Registro.objects.filter(user=request.user)
    tamanio = len(datoregistros)
    if request.method == 'GET':
        return render(request, 'crearRegistroEfectivo.html', {'form': registroEfectivo(), 'tamanio': tamanio})
    else:
        try:
            form = registroEfectivo(request.POST)
            nuevoRegistro = form.save(commit=False)
            nuevoRegistro.efectivosaldo = Registro.objects.filter(user=request.user).last().efectivosaldo
            if nuevoRegistro.efectivosaldo is None:
                for i in Registro.objects.filter(user=request.user):
                    if i.efectivosaldo is not None:
                        nuevoRegistro.efectivosaldo = i.efectivosaldo
                        break
            if nuevoRegistro.efectivoingresos is not None:
                nuevoRegistro.efectivosaldo = nuevoRegistro.efectivosaldo + nuevoRegistro.efectivoingresos
            else:
                nuevoRegistro.efectivoingresos = 0.0
            if nuevoRegistro.efectivoegresos is not None:
                nuevoRegistro.efectivosaldo = nuevoRegistro.efectivosaldo - nuevoRegistro.efectivoegresos   
                if nuevoRegistro.efectivosaldo < 0:
                    return render(request, 'crearRegistroEfectivo.html', {'form': registroEfectivo(), 'error': 'El saldo no puede ser negativo', 'tamanio': tamanio})
            else:
                nuevoRegistro.efectivoegresos = 0.0
            nuevoRegistro.bancosaldo = Registro.objects.filter(user=request.user).last().bancosaldo 
            if nuevoRegistro.bancosaldo is None:
                for i in Registro.objects.filter(user=request.user):
                    if i.bsaldo is not None:
                        nuevoRegistro.bancosaldo = i.bancosaldo
                        break
            if nuevoRegistro.bancoingresos is not None:
                nuevoRegistro.bancosaldo = nuevoRegistro.bancosaldo + nuevoRegistro.bancoingresos
            else:
                nuevoRegistro.bancoingresos = 0.0
            if nuevoRegistro.bancoegresos is not None:
                nuevoRegistro.bancosaldo = nuevoRegistro.bancosaldo - nuevoRegistro.bancoegresos
                if nuevoRegistro.bancosaldo < 0:
                    return render(request, 'crearRegistroEfectivo.html', {'form': registroEfectivo(), 'error': 'El saldo no puede ser negativo', 'tamanio': tamanio})
            else:
                nuevoRegistro.bancoegresos = 0.0
            nuevoRegistro.user = request.user
            nuevoRegistro.save()

            return redirect('principalusuarios')
        except ValueError:
            return render(request, 'crearRegistroEfectivo.html', {'form': registroEfectivo(),  'error': 'Datos incorrectos', 'tamanio': tamanio})

def crearRBanco(request):
    datoregistros = Registro.objects.filter(user=request.user)
    tamanio = len(datoregistros)
    if request.method == 'GET':
        return render(request, 'crearRegistroBanco.html', {'form': registroBanco(), 'tamanio': tamanio})
    else:
        try:
            form = registroBanco(request.POST)
            nuevoRegistro = form.save(commit=False)
            nuevoRegistro.efectivosaldo = Registro.objects.filter(user=request.user).last().efectivosaldo
            if nuevoRegistro.efectivosaldo is None:
                for i in Registro.objects.filter(user=request.user):
                    if i.efectivosaldo is not None:
                        nuevoRegistro.efectivosaldo = i.efectivosaldo
                        break
            if nuevoRegistro.efectivoingresos is not None:
                nuevoRegistro.efectivosaldo = nuevoRegistro.efectivosaldo + nuevoRegistro.efectivoingresos
            else:
                nuevoRegistro.efectivoingresos = 0.0
            if nuevoRegistro.efectivoegresos is not None:
                nuevoRegistro.efectivosaldo = nuevoRegistro.efectivosaldo - nuevoRegistro.efectivoegresos  
                if nuevoRegistro.efectivosaldo < 0:
                    return render(request, 'crearRegistroBanco.html', {'form': registroBanco(), 'error': 'El saldo no puede ser negativo', 'tamanio': tamanio}) 
            else:
                nuevoRegistro.efectivoegresos = 0.0
            nuevoRegistro.bancosaldo = Registro.objects.filter(user=request.user).last().bancosaldo 
            if nuevoRegistro.bancosaldo is None:
                for i in Registro.objects.filter(user=request.user):
                    if i.bancosaldo is not None:
                        nuevoRegistro.bancosaldo = i.bancosaldo
                        break
            if nuevoRegistro.bancoingresos is not None:
                nuevoRegistro.bancosaldo = nuevoRegistro.bancosaldo + nuevoRegistro.bancoingresos
            else:
                nuevoRegistro.bancoingresos = 0.0
            if nuevoRegistro.bancoegresos is not None:
                nuevoRegistro.bancosaldo = nuevoRegistro.bancosaldo - nuevoRegistro.bancoegresos
                if nuevoRegistro.bancosaldo < 0:
                    return render(request, 'crearRegistroBanco.html', {'form': registroBanco(), 'error': 'El saldo no puede ser negativo', 'tamanio': tamanio})
            else:
                nuevoRegistro.bancoegresos = 0.0
            nuevoRegistro.user = request.user
            nuevoRegistro.save()

            return redirect('principalusuarios')
        except ValueError:
            return render(request, 'crearRegistroBanco.html', {'form': registroBanco(),  'error': 'Datos incorrectos', 'tamanio': tamanio})
    
def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'iniciosesion.html', {'form': AuthenticationForm()})
    else:
        user = auth_authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('principalusuarios')
        else:
            return render(request, 'iniciosesion.html', {'form': AuthenticationForm(),'error': 'Usuario o contraseña incorrectos'})
    
def cerrarsesion(request):
    auth_logout(request)
    return redirect('base')
    