from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Estudiante
from django import forms

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'universidad']

def student_list(request):
    students = Estudiante.objects.all()
    return render(request, 'asistentes/student_list.html', {'students': students})

def student_register(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = EstudianteForm()
    return render(request, 'asistentes/student_register.html', {'form': form})

