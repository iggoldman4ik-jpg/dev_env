from contextlib import redirect_stderr
import decimal

from django.contrib import auth
from django.contrib.admin import action
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from main.forms import RegisterForm, UserLoginForm
from main.models import Users
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username= request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:menu"))
    else: 
        logout(request)
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'main/index.html', context)

def registration(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("main:index"))
    else:
        form = RegisterForm()
    return render(request, 'main/registration.html', {'form': form})

def menu(request):
    if not request.user.is_authenticated:
        return redirect(reverse("main:index"))
    context = {"user": request.user,
                                "history": [{"type": "Пополнение", "money": "+200"}, 
                                            {"type": "Снятие", "money": "-100"},
                                            {"type": "Перевод", "money": "-50"}]}
    if request.method == "GET":
        action = request.GET.get("action")
        if action == "add" or action == "withdraw":
            target_url =  f"../operations/?operation={action}"
            return redirect(target_url)
    if request.method == "POST":
        pass#context = {"username": "test123"}
    return render(request, 'main/menu.html', context)



#press f funk operation😒 