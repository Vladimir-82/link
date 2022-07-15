from django.views.generic.edit import CreateView

from django.shortcuts import render
from .models import Link
from .forms import AddForm


def create(request):
    if request.method == 'GET':
        form = AddForm()
        return render(request, 'app/create.html', {'form': form})
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        links = Link.objects.last()
        return render(request, 'app/create.html', {'links': links})