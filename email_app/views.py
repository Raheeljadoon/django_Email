from django.shortcuts import render
from . import forms
from django.core.mail import send_mail
from django.shortcuts import render
from email_sender.settings import EMAIL_HOST_USER


def email(request):

    email_form = forms.Email_form()

    if request.method == 'POST':

        email_form = forms.Email_form(request.POST)

        subject = "Welcome to Raheel project"
        message = "I am testin this app for practice"
        recepient = str(email_form['email'].value())
        send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)

        return render(request,'email/success.html',{'recepient':recepient})

    return render (request, 'email/index.html', {'form': email_form})

