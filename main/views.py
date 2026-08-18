import decimal

from django.contrib.admin import action
from django.shortcuts import render
from django.template import context
from main.models import Users

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def registration(request):
    return render(request, 'main/registration.html')

def menu(request):
    context = {"username": "test123", 
                                "history": [{"type": "Пополнение", "money": "+200"}, 
                                            {"type": "Снятие", "money": "-100"},
                                            {"type": "Перевод", "money": "-50"}]}
    if request.method == "POST":
        user = Users.objects.get(id=1)
        action = request.POST.get("action")
        input_info=request.POST.get("input_field")
        if action == "add":
            user.balance += decimal.Decimal(input_info)
            user.save()
        elif action == "withdraw":
            user.balance -= decimal.Decimal(input_info)
            user.save()
    if request.method == "GET":
        pass#context = {"username": "test123"}
    return render(request, 'main/menu.html', context)

#press f funk operation😒 