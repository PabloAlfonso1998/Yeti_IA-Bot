from django.shortcuts import render

# Create your views here.
def index_temario(request):
    Temario.objects.all()
return(request, template_name='temario/index.html')

def crear_tema(request):
    if request.method == 'post':
        numero = request.POST['numero']
        numero = request.POST['nombre']
        Temario.objects.create(numero=numero, nombre=nombre)
return render(request, 'temario/create.html')
