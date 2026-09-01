from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Tecnico, Equipo, Reparacion
from .forms import ClienteForm, EquipoForm, TecnicoForm, ReparacionForm, ClientesFilter, EquipoFilter, TecnicoFilter, ReparacionFilter
from django.db import models


# Create your views here.
def index(request):
    context = {"mensaje":"Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request,"myapp/index.html",context)

     

def clientes(request):
    query = request.GET.get('q')  # Captura lo que se escribe en el buscador
    
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:clientes")
    else:
        form = ClienteForm()

    if query:
        clientes = Cliente.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(email__icontains=query)
        )
    else:
        clientes = Cliente.objects.all()

    return render(
        request,
        "myapp/clientes.html",
        {
            "clientes": clientes,
            "form": form,
            "query": query,
        },
    )


def equipos(request):
    query = request.GET.get('q')
    
    if request.method == "POST":
        form = EquipoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myapp:equipos")
    else:
        form = EquipoForm()

    if query:
        equipos = Equipo.objects.filter(
            models.Q(cliente__nombre__icontains=query) |
            models.Q(tipo__icontains=query) |
            models.Q(marca__icontains=query) |
            models.Q(modelo__icontains=query)
        )
    else:
        equipos = Equipo.objects.all()

    return render(
        request,
        "myapp/equipos.html",
        {
            "equipos": equipos,
            "form": form,
            "query": query,
        },
    )


def tecnicos(request):
    query = request.GET.get('q')
    
    if request.method == "POST":
        form = TecnicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myapp:tecnicos")
    else:
        form = TecnicoForm()

    if query:
        tecnicos = Tecnico.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(telefono__icontains=query)
        )
    else:
        tecnicos = Tecnico.objects.all()

    return render(
        request,
        "myapp/tecnicos.html",
        {
            "tecnicos": tecnicos,
            "form": form,
            "query": query,
        },
    )


def reparaciones(request):
    query = request.GET.get('q')
    
    if request.method == "POST":
        form = ReparacionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myapp:reparaciones")
    else:
        form = ReparacionForm()

    if query:
        reparaciones = Reparacion.objects.filter(
            models.Q(equipo__numero_serie__icontains=query) |
            models.Q(tecnico__nombre__icontains=query) |
            models.Q(estado__icontains=query)
        )
    else:
        reparaciones = Reparacion.objects.all()

    return render(
        request,
        "myapp/reparacion.html",
        {
            "reparaciones": reparaciones,
            "form": form,
            "query": query,
        },
    )
def eliminar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == "POST":
        reparacion.delete()
        return redirect("myapp:reparaciones")

    return render(
        request,
        "myapp/confirmar_eliminacion.html",
        {"reparacion": reparacion},
    )

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        form = ClientesFilter(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('myapp:clientes')
    else:
        form = ClientesFilter(instance=cliente)
    
    return render(request, 'myapp/editar_cliente.html', {'form': form, 'cliente': cliente})


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('myapp:clientes')
    
    return render(request, 'myapp/clientes.html', {'cliente': cliente})


def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    
    if request.method == 'POST':
        form = EquipoFilter(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('myapp:equipos')
    else:
        form = EquipoFilter(instance=equipo)
    
    return render(request, 'myapp/editar_equipo.html', {'form': form, 'equipo': equipo})


def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    
    if request.method == 'POST':
        equipo.delete()
        return redirect('myapp:equipos')
    
    return render(request, 'myapp/equipos.html', {'equipo': equipo})


def editar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    
    if request.method == 'POST':
        form = TecnicoFilter(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('myapp:tecnicos')
    else:
        form = TecnicoFilter(instance=tecnico)
    
    return render(request, 'myapp/editar_tecnico.html', {'form': form, 'tecnico': tecnico})


def eliminar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    
    if request.method == 'POST':
        tecnico.delete()
        return redirect('myapp:tecnicos')
    
    return render(request, 'myapp/tecnicos.html', {'tecnico': tecnico})


def editar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)
    
    if request.method == 'POST':
        form = ReparacionFilter(request.POST, instance=reparacion)
        if form.is_valid():
            form.save()
            return redirect('myapp:reparaciones')
    else:
        form = ReparacionFilter(instance=reparacion)
    
    return render(request, 'myapp/editar_reparacion.html', {'form': form, 'reparacion': reparacion})


def eliminar_reparacion_nuevo(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)
    
    if request.method == 'POST':
        reparacion.delete()
        return redirect('myapp:reparaciones')
    
    return render(request, 'myapp/reparacion.html', {'reparacion': reparacion})