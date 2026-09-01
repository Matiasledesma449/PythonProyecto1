from django.urls import path


from . import views


app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('equipos/', views.equipos, name='equipos'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('reparaciones/', views.reparaciones, name='reparaciones'),
    path("reparaciones/<int:id>/eliminar/", views.eliminar_reparacion, name="eliminar_reparacion"),
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('equipo/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipo/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('tecnico/editar/<int:id>/', views.editar_tecnico, name='editar_tecnico'),
    path('tecnico/eliminar/<int:id>/', views.eliminar_tecnico, name='eliminar_tecnico'),
    path('reparacion/editar/<int:id>/', views.editar_reparacion, name='editar_reparacion'),
    path('reparacion/eliminar/<int:id>/', views.eliminar_reparacion_nuevo, name='eliminar_reparacion_nuevo'),
]
