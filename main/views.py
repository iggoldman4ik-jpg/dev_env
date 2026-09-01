from contextlib import redirect_stderr
import decimal

from django.contrib.admin import action
from django.shortcuts import redirect, render, reverse
from django.template import context
from main.models import Users

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def registration(request):
    return render(request, 'main/registration.html')

def menu(request):
    context = {"username": "test123",
                                "balance": "12345",
                                "history": [{"type": "Пополнение", "money": "+200"}, 
                                            {"type": "Снятие", "money": "-100"},
                                            {"type": "Перевод", "money": "-50"}]}
    if request.method == "GET":
        action = request.GET.get("action")
        target_url =  f"{reverse("pay-page")}?operation={action}"
        redirect(target_url)
    if request.method == "POST":
        pass#context = {"username": "test123"}
    return render(request, 'main/menu.html', context)



#press f funk operation😒 