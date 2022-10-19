from django.urls import path
from app1.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('vuelo/', vuelo),
    path('personal/', personal),
    path('pasajero/', pasajero),
    path('sobrenostros', sobrenosotros, name="Sobrenosotros"),

#URL DE CREACION
    path('formulario1/', formulariovuelo, name="Crear Vuelos"),
    path('formulario2/', formulariopersonal, name="Crear Personal"),
    path('formulario3/', formulariopasajero, name="Crear Pasajeros"),

#URL DE LEER
    path('leerVuelos/',leerVuelos, name="Leer Vuelos"),
    path('leerPersonal/',leerPersonal, name="Leer Personal"),
    path('leerPasajeros/',leerPasajero, name="Leer Pasajeros"),

#URL DE EDICION
    path('editaVuelo/<numVuelo>/', editaVuelo, name = "EditaVuelo"),
    path('editarPersonal/<profesionPersonal>/', editarPersonal, name = "EditarPersonal"),
    path('editarPasajero/<idvueloPasajero>/', editarPasajero, name = "EditarPasajero"),

#URL DE ELIMINACION
    path('eliminaVuelo/<numVuelo>/', eliminaVuelo, name = "EliminaVuelo"),
    path('eliminaPersonal/<profesionPersonal>/', eliminaPersonal, name = "EliminaPersonal"),
    path('eliminaPasajero/<idvueloPasajero>/', eliminaPasajero, name = "EliminaPasajero"),

#URL DE BUSQUEDAS
    path('bus/', bus, name="Buscar"),
    path('buscarVuelos/', busquedaVuelos, name="Buscar Vuelos"),
    path('buscarPersonal/', busquedaPersonal, name="Buscar Personal"),
    path('buscarPasajero/', busquedaPasajero, name="Buscar Pasajeros"),
##
    path('buscar_pasa/',buscar_pasa),
    path('buscar_per/',buscar_per),
    path('buscar/',buscar),

#URL DE LOGIN Y LOGOUT
    path('login/',InicioSesion, name="Login"),
    path('registro/',registro, name="Registrarse"),
    path('logout/', LogoutView.as_view(template_name="app1/logout.html"), name="Logout"),

#URL DE EDICIONUSUARIO
    path('editUser/',editarUsuario, name="Editar Usuario"),
    path('avatar/', agregarAvatar, name="Avatar"),

    ]