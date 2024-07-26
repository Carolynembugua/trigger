from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def payment(request):
    return render(request,'payment.html')
def information(request):
    return render(request,'information.html')