from unicodedata import decomposition
from django.shortcuts import render
from django.http import HttpResponse

from app1.models import *
from app1.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #se importa el AuthenticationForm para el inicio de sesion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

############
#  INICIO  #
############

def inicio(request):
    return render(request,'app1/inicio.html')


############
#  LOGIN  #
############

def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            if user:
                login(request, user)
                return render(request, "app1/inicio.html", {"mensaje":f"Bienvenido {user}"})
        else:
            return render(request, "app1/inicio.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "app1/login.html", {"f1":form})

def registro(request):
    if request.method == "POST":
        formu = FormularioRegistro(request.POST)
        if formu.is_valid():
            username = formu.cleaned_data["username"]
            formu.save()
            return render(request, "app1/inicio.html", {"mensaje": f"Usuario {username} creado."})
    else:
        formu = FormularioRegistro()
    return render(request, "app1/registro.html", {"f2":formu})



############
#  VUELOS  #
############

def vuelo(request):
    return render(request,'app1/vuelo.html')

#CREACION DE VUELOS
def formulariovuelo(request):
    if request.method=="POST":#si yo le doy al boton GO
        formulariovuelo = FormuVuelo(request.POST)
        if formulariovuelo.is_valid():
            info = formulariovuelo.cleaned_data
            vuelof = Vuelo(id_vuelo = info["id_vuelo"], salida = info["salida"], destino = info["destino"], fecha = info["fecha"], hora_de_salida = info["hora_de_salida"])#lee la informacion de las cajas de texto
            vuelof.save()#guardar en la base de datos
            return render(request,"app1/inicio.html")#despues de enviar salta esta pagina
    else:
        formulariovuelo = FormuVuelo()
    return render(request,"app1/FVuelo.html",{"formulario1":formulariovuelo})#cuando entro a la pagina web por primera vez sale este return

#BUSQUEDA DE VUELOS
def busquedaVuelos(request):
    return render(request,"app1/busquedaVuelos.html")


def buscar(request):
    if request.GET["salida"]:
        busqueda = request.GET["salida"]
        vuelos = Vuelo.objects.filter(salida=busqueda)#puede ir tambien camada__icontains = busqueda
        return render(request,"app1/vuelo_b.html",{"vuelos":vuelos, "busqueda":busqueda})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando el vuelo que sale de: {busqueda}")

@login_required
#LEER VUELOS
def leerVuelos(request):
    fly = Vuelo.objects.all()
    contexto = {"fly":fly}
    return render(request,"app1/vuelo.html",contexto)

#ELIMINAR VUELOS
def eliminaVuelo(request, numVuelo):
    idvuelo= Vuelo.objects.get(id_vuelo=numVuelo)
    idvuelo.delete()
    vuelos = Vuelo.objects.all()
    contextov = {"fly":vuelos}
    return render (request, "App1/vuelo.html", contextov)

#EDITAR VUELOS
def editaVuelo(request, numVuelo):
    idvuelo = Vuelo.objects.get(id_vuelo=numVuelo)

    if request.method == "POST":
        formulariovuelo = FormuVuelo(request.POST)
        if formulariovuelo.is_valid():
            
            info = formulariovuelo.cleaned_data
            
            idvuelo.id_vuelo = info["id_vuelo"]
            idvuelo.salida = info["salida"]
            idvuelo.destino = info["destino"]
            idvuelo.fecha = info["fecha"]
            idvuelo.hora_de_salida = info["hora_de_salida"]

            idvuelo.save()
            return render(request,"app1/inicio.html")
    else:
        formulariovuelo = FormuVuelo(initial={"id_vuelo":idvuelo.id_vuelo,"salida":idvuelo.salida,
        "destino": idvuelo.destino, "fecha": idvuelo.fecha, "hora_de_salida": idvuelo.hora_de_salida })
    return render(request,"app1/editarVuelo.html", {"formulario1":formulariovuelo, "idVuelo": numVuelo})


############
# PERSONAL #
############

@login_required
def personal(request):
    return render(request,'app1/personal.html')

#CREACION DE PERSONAL
def formulariopersonal(request):
    if request.method=="POST":
        formulariopersonal = FormuPersonal(request.POST)
        if formulariopersonal.is_valid():
            info = formulariopersonal.cleaned_data
            personalf = Personal(nombre = info["nombre"], apellido = info["apellido"], profesion = info["profesion"],  id_vuelo = info["id_vuelo"])
            personalf.save()
            return render(request,"app1/inicio.html")
    else:
        formulariopersonal = FormuPersonal()
    return render(request,"app1/FPersonal.html",{"formulario2":formulariopersonal})

#BUSQUEDA DE PERSONAL
def busquedaPersonal(request):
    return render(request,"app1/busquedaPersonal.html")


def buscar_per(request):
    if request.GET["profesion"]:
        busqueda_per = request.GET["profesion"]
        personas = Personal.objects.filter(profesion = busqueda_per)
        return render(request,"app1/personal_b.html",{"personas":personas, "busqueda_per":busqueda_per})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando la profesión: {busqueda_per}")

@login_required
#LEER PERSONAL
def leerPersonal(request):
    persona = Personal.objects.all()
    contexto = {"persona":persona}
    return render(request,"app1/personal.html",contexto)

#ELIMINAR PERSONAL
def eliminaPersonal(request, profesionPersonal):
    profesionPe= Personal.objects.get(profesion=profesionPersonal)
    profesionPe.delete()
    personalElim = Personal.objects.all()
    contextoPe = {"staff":personalElim}
    return render (request, "App1/personal.html", contextoPe)

#EDITAR PERSONAL
def editarPersonal(request, profesionPersonal):
    profesion= Personal.objects.get(profesion=profesionPersonal)

    if request.method=="POST":
        formulariopersonal = FormuPersonal(request.POST)
        if formulariopersonal.is_valid():
            
            info = formulariopersonal.cleaned_data
           
            profesion.nombre = info["nombre"]
            profesion.apellido = info["apellido"]
            profesion.profesion = info["profesion"]
            profesion.id_vuelo = info["id_vuelo"]

            profesion.save()
            return render(request,"app1/inicio.html")
    else:
        formulariopersonal = FormuPersonal(initial={"nombre":profesion.nombre,"apellido":profesion.apellido,
        "profesion":profesion.profesion, "id_vuelo":profesion.id_vuelo})
    return render(request,"app1/editarPersonal.html",{"formulario2":formulariopersonal, "profesionPersonal": profesionPersonal })  




############
# PASAJERO #
############


def pasajero(request):
    return render(request,'app1/pasajero.html')

# CREACION DE PASAJERO
def formulariopasajero(request):
    if request.method=="POST":
        formulariopasajero = FormuPasajero(request.POST)
        if formulariopasajero.is_valid():
            info = formulariopasajero.cleaned_data
            editPersonal = Pasajero(nombre = info["nombre"], apellido = info["apellido"], documento = info["documento"], id_vuelo = info["id_vuelo"])
            editPersonal.save()
            return render(request,"app1/inicio.html")
    else:
        formulariopasajero = FormuPasajero()
    return render(request,"app1/FPasajero.html",{"formulario3":formulariopasajero})

#BUSQUEDA DE PASAJERO
def busquedaPasajero(request):
    return render(request,"app1/busquedaPasajero.html")


def buscar_pasa(request):
    if request.GET["id_vuelo"]:
        busqueda_pasa = request.GET["id_vuelo"]
        pasajeros = Pasajero.objects.filter(id_vuelo = busqueda_pasa)
        return render(request,"app1/pasajero_b.html",{"pasajeros":pasajeros, "busqueda_pasa":busqueda_pasa})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando los pasajeros del vuelo: {busqueda_pasa}")

@login_required
#LEER PASAJERO
def leerPasajero(request):
    pasa = Pasajero.objects.all()
    contexto = {"pasa":pasa}
    return render(request,"app1/pasajero.html",contexto)  

#ELIMINAR PASAJERO
def eliminaPasajero(request, idvueloPasajero):
    elimPasajero= Pasajero.objects.get(id_vuelo=idvueloPasajero)
    elimPasajero.delete()

    pasajeroElim = Pasajero.objects.all()
    contextoPa = {"staff":pasajeroElim}
    return render (request, "App1/pasajero.html", contextoPa)

#EDITAR PASAJERO
def editarPasajero(request, idvueloPasajero):
    editPasajero= Pasajero.objects.get(id_vuelo=idvueloPasajero)
    if request.method=="POST":
        
        formulariopasajero = FormuPasajero(request.POST)
        
        if formulariopasajero.is_valid():
            info = formulariopasajero.cleaned_data

            editPasajero.nombre = info["nombre"]
            editPasajero.apellido = info["apellido"]
            editPasajero.documento = info["documento"]
            editPasajero.id_vuelo = info["id_vuelo"]

            editPasajero.save()
            return render(request,"app1/inicio.html")
    else:
        formulariopasajero = FormuPasajero(initial={"nombre": editPasajero.nombre, "apellido": editPasajero.apellido,
        "documento": editPasajero.documento, "id_vuelo":editPasajero.id_vuelo })
    return render(request,"app1/editarPasajero.html",{"formulario3":formulariopasajero, "idvueloPasajero": idvueloPasajero })

@login_required
#BUSCADOR
def bus(request):
    return render(request,"app1/buscar.html")
