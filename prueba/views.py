from django.shortcuts import render
from .forms import *

# Create your views here.
def crear_producto(request):
    producto_form = ProductoForm()
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto = producto_form.save()
    else:
        context = {
            'form': producto_form,
        } 
    return render(request, 'crear_producto.html', context)
