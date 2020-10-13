from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        if (len(name)<2 or len(email)<7 or len(phone)<10 or len(message)<20):
            messages.error(request,'Please fill the form correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, message=message, timestamp=timestamp)
            contact.save()
            messages.success(request, 'Your form has been submitted. Thank You!')

    return render(request, 'Home/contact.html')
