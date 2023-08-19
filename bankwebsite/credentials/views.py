from django.contrib import auth, messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from .models import District, Branch, AccountType, Material
from .forms import Application_l


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("form")
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, "login.html")


def application_form_view(request):
    districts = District.objects.all()
    account_types = AccountType.objects.all()
    materials = Material.objects.all()

    if request.method == 'POST':
        form_class = Application_l
        form = Application_l(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted')
            return render(request, 'application_form.html', {'form': Application_l(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = Application_l()

    return render(request, 'application_form.html', {
        'form': form,
        'districts': districts,
        'account_types': account_types,
        'materials': materials,
    })


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name taken")
                return redirect("register")

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect("register")

    return render(request, 'register.html')


def success(request):
    return render(request, 'success.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
