from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.index, name="index"),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
]