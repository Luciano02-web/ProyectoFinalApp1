from django import forms


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