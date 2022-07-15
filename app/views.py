import uuid

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

        hash = uuid.uuid3(uuid.NAMESPACE_DNS, links.link)
        new_link = hash.__str__()[:8]
        links.shortlink = ''.join(('https://', 'mydomen/', new_link))
        links.save()
        
        return render(request, 'app/create.html', {'links': links})