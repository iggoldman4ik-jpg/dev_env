import decimal

from django.shortcuts import render
from django.template import context
from main.models import Users

# Create your views here.
def pay_page(request):
    operation = request.GET.get("operation")
    if operation == "add":
        context={"operation_title": "Пополнение",
                                "operation_type": "add",
                                "operation_button": "Пополнить🤑"}
    else:
       context={"operation_title": "Cнятие",
                                       "operation_type": "withdraw",
                                       "operation_button": "Пополнить🤑"}  

    
    if request.method == "GET":
        pass
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
    return render(request, 'operations_app/pay_page.html', context)