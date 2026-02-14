from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm



def profile(self, request):
    ...

def home(request):
    return render(request, 'blog/base.html')


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

