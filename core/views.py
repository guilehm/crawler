from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def logout_view(request):
    logout(request)
    return redirect('core:index')


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            login(request, authenticated_user)
            return redirect('core:index')
    return render(request, 'core/accounts/login.html', {
        'form': form,
    })


def index(request):
    return render(request, 'core/index.html')
