from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact(request):
    if request.method == 'POST':
        objet = request.POST['objet']
        email = request.POST['email']
        message = request.POST['message'] + "\n Ce message a été envoyé par " + email
        send_mail(
            objet,
            message,
            email,
            ['raniachettab3@gmail.com'],
        )
    return render(request, 'contact.html', {})