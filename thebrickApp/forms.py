from django.forms import (Form,
EmailField, 
EmailInput, 
CharField, 
PasswordInput,
BooleanField,
CheckboxInput,
TextInput
)
from django.contrib.auth.forms import BaseUserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Producto


   
class FormularioRegistro(BaseUserCreationForm):
    def __init__(self, *args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['password1'].widget.attrs = { 'class': 'form-control' }
        self.fields['password2'].widget.attrs = { 'class': 'form-control' }
        
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name', 
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username' : TextInput( attrs = { 'class':'form-control' }),
            'first_name' : TextInput( attrs = { 'class':'form-control' }),
            'last_name' : TextInput( attrs = { 'class':'form-control' }),
            'email' : EmailInput( attrs = { 'class':'form-control' }),
            'password1' : PasswordInput( attrs = { 'class':'form-control'}),
            'password2' : PasswordInput( attrs = { 'class':'form-control'})
        }


class FormularioLogin(Form):
    correo_usuario = EmailField(
        required=True,
        label = 'Ingrese su correo',
        widget = EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'name@example.com'
            }
        )
    )
    contrasenia_usuario = CharField(
        required=True,
        min_length=4,
        max_length=16,
        label='Ingrese su contraseña',
        widget=PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
    recuerdame = BooleanField(
        required=False,
        label = "Recuerdame",
        widget = CheckboxInput()
    )
    
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto 
        fields = '__all__'

