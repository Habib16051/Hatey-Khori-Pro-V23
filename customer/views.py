from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)