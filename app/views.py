from django.views.generic.edit import CreateView

from django.shortcuts import render
from .models import Link
from .forms import AddForm





def index(request):
    result = Link.objects.all()
    return render(request, 'app/index.html', {'result': result})


class AddCreateView(CreateView):
    template_name = 'app/create.html'
    form_class = AddForm
    success_url = ''