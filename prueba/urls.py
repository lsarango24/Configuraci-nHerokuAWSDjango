
from django.urls import path
from django.conf.urls import url 
from prueba import views
from prueba.views import ListarProducto

urlpatterns = [
    path(r'', views.crear_producto, name='crear_producto'),
    path('Listar/', ListarProducto.as_view(), name='ListarProducto'),
    path('Eliminar/<int:pk>', views.eliminar, name='eliminar'),

]