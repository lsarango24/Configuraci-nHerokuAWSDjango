from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

# Create your views here.
def crear_producto(request):
    producto_form = ProductoForm()
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST or None, request.FILES or None)
        if producto_form.is_valid():
            print("entro")
            producto_form.save()
            return redirect('ListarProducto')
    
    context = {
        'form': producto_form,
    }
        
     
    return render(request, 'crear_producto.html', context )

class crear_product(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('crear_producto')

class ListarProducto(ListView):
    model = Producto
    template_name = "ver_producto.html"