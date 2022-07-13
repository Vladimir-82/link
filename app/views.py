from django.views.generic.edit import CreateView

from django.shortcuts import render
from .models import Link
from .forms import AddForm



def index(request):
    links = Link.objects.all()
    return render(request, 'app/index.html', {'links': links})


# class AddCreateView(CreateView):
#     template_name = 'app/create.html'
#     form_class = AddForm
#     success_url = ''



def linker(request):
    print(request.POST)
    if request.method == 'POST':
        print('post here')
        form = AddForm(request.POST)
        if form.is_valid():
            print('ffffffffffffffffff')
            form.save()

            return render(request, 'app/index.html')

    else:
        form = AddForm()
        context = {'form': form}
        print('get here')
        
        return render(request, 'app/create.html', context)