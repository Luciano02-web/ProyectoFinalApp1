from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app1.models import Avatar


class FormuVuelo(forms.Form):
    id_vuelo = forms.IntegerField()
    salida = forms.CharField(max_length=50)
    destino = forms.CharField(max_length=50)
    fecha = forms.DateField()    #2022-05-23(AAAA-MM-DD)
    hora_de_salida = forms.TimeField() #02:13(HH:MM)


class FormuPersonal(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=50)
    id_vuelo = forms.IntegerField()

class FormuPasajero(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    documento = forms.IntegerField()
    id_vuelo = forms.IntegerField()

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label='Ingrese email')
    first_name= forms.CharField(label='Ingrese nombre')
    last_name= forms.CharField(label='Ingrese apellido')
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField(label='Ingrese email')
    first_name= forms.CharField(label='Ingrese nombre')
    last_name= forms.CharField(label='Ingrese apellido')
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name","last_name","email","password1","password2"]

class FormuAvatar(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["usuario", "imagen"]