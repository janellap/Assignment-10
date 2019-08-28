from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Dog
from .forms import DogForm

from .models import Owner

def index(request):
    ownerObject = Owner.objects.get(ownerid=1)
    dogObjects = Dog.objects.all()
    context = {'dogs': dogObjects, 'owner': ownerObject}
    return render(request, 'dogs_project/index.html', context)

#def new_dogname(request):
    #new_dogname = new_dogname.objects.order_by('dog_name')
    #context = {'new_dogname': new_dogname}
    #return render(request, 'dogs_projet/new_dogname.html', context)

def new_dogname(request):
    if request.method != 'Post' :
        form = DogForm()
    else:
        form = DogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dogs_project:new_dogname'))

    context = {'form': form}
    return render(request, 'dogs_project/new_dogname.html', context)