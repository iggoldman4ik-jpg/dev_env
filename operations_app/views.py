import decimal

from django.db import transaction
from django.shortcuts import render
from django.template import context
from main.models import Operation, Users

# Create your views here.
def pay_page(request):
    operation = request.GET.get("operation")
    if operation == "add":
        context={"operation_title": "Пополнение",
                                "operation_type": "add",
                                "operation_button": "Пополнить🤑"}
    elif operation == "withdraw":
       context={"operation_title": "Cнятие",
                                       "operation_type": "withdraw",
                                       "operation_button": "Снять🤑"}

       
    
    if request.method == "GET":
        if operation == "transfer":
            return render(request, 'operations_app/transfer_page.html')
    if request.method == "POST":
        user = Users.objects.get(id = request.user.id)
        action = request.POST.get("action")
        amount=request.POST.get("amount")
        if action == "add":
            with transaction.atomic():
                user.balance += decimal.Decimal(amount)
                user.save()
                Operation.objects.create(
                    user = request.user,
                    amount = decimal.Decimal(amount),
                    operation_type = Operation.Type.DEPOSIT
                )
        elif action == "withdraw":
            with transaction.atomic():
                user.balance -= decimal.Decimal(amount)
                user.save()
                Operation.objects.create(
                    user = request.user,
                    amount = decimal.Decimal(amount),
                    operation_type = Operation.Type.WITHDRAW
                )
        elif action == "transfer":
            with transaction.atomic():
                user.balance -= decimal.Decimal(amount)
                user.save()
                recipient_name = request.POST.get("recipient")
                recipient = Users.objects.get(username = recipient_name)
                recipient.balance += decimal.Decimal(amount)
                recipient.save()
                Operation.objects.create(
                    user = request.user,
                    amount = decimal.Decimal(amount),
                    operation_type = Operation.Type.TRANSFER,
                    receiver = recipient
                )
            return render(request, 'operations_app/transfer_page.html')
    return render(request, 'operations_app/pay_page.html', context)