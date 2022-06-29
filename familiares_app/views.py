from django.shortcuts import render
from familiares_app.models import Familiar

def listar_familiares(request):
    context = {}
    context["familiares"] = Familiar.objects.all()
    return render(request, "familiares_app/lista_familiares.html", context)
