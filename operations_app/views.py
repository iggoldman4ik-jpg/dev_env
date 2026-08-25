from django.shortcuts import render

# Create your views here.
def pay_page(request):
    return render(request, 'main/pay_page.html')