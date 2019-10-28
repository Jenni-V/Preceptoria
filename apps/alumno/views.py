from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Alumno
from .forms import SignUpForm
from .serializers import AlumnoSerializer
from rest_framework import generics
from django.views.generic.list import ListView

class SignUpView(CreateView):
    model = Alumno
    form_class = SignUpForm

    def form_valid(self, form):
        
        # En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')


class AlumnoList(generics.ListAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

  


