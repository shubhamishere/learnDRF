from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "variable": "this is sent",
        "variable2": "this is nice"
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')

def contact(request):
    #contact page ka post request yaha pe aaega, fir humein logic lga ke DB mein save karwana hai jo data aa rha hai POST mein.
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        messages.success(request, "your message has been sent")

    return render(request, 'contact.html')