from django.shortcuts import render
from .models import contactForm,contactInfo

# Create your views here.
def contact(request):
    #Fetching Data from database
    if request.method == 'POST':
        fullName = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactData = contactForm(fullName=fullName,email=email,subject=subject,message=message)
        contactData.save()
    contactInfoData = contactInfo.objects.all()
    context = {
        'contactInfo': contactInfoData
    }
    return render(request,'contact.html',context)