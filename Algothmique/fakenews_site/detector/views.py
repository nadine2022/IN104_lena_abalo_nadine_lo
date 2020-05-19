from .forms import detectForm
from django.shortcuts import render

def det(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = detectForm(request.POST or None)
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'detector/det.html', locals())
