from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView

# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'
    
#self-defined rigister function
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form':form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)