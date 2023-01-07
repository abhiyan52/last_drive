
from django.shortcuts import render, redirect

from artifacts.forms import ArtifactForm
from artifacts.models import Artifact


def index(request):
    documents = Artifact.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = ArtifactForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArtifactForm()
    return render(request, 'index.html', {
        'form': form,
        "documents": documents
    })
