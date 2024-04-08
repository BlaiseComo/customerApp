from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from .forms import PreWorkoutForm

# Create your views here.
def index(request):

    return render(request, 'customer_app/index.html')

class PreWorkoutListView(generic.ListView):
    model = PreWorkout

class PreWorkoutDetailView(generic.DetailView):
    model = PreWorkout

def create_preworkout(request):
    if request.method == 'POST':
        form = PreWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preworkouts')
    else:
        form = PreWorkoutForm()

    return render(request, 'customer_app/create_preworkout.html', {'form': form})

def update_preworkout(request, id):
    preworkout = get_object_or_404(PreWorkout, pk=id)
    if request.method == 'POST':
        form = PreWorkoutForm(request.POST, instance=preworkout)
        if form.is_valid():
            form.save()
            return redirect('preworkouts') 
    else:
        form = PreWorkoutForm(instance=preworkout)
    
    return render(request, 'customer_app/update_preworkout.html', {'form': form, 'preworkout': preworkout})

def delete_preworkout(request, id):
    preworkout = get_object_or_404(PreWorkout, pk=id)
    if request.method == 'POST':
        preworkout.delete()
        return redirect('preworkouts')  
