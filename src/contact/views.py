from django.shortcuts import render
from django.core.mail import send_mail

from .forms import contactForm

from ecomtest import settings

# Create your views here.

def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print(form.cleaned_data['email'], settings.EMAIL_HOST_USER)
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'MEssage from ME'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        """send_mail(
            'Subject here',
            'Here is the message',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )"""
        title = "Thanks!"
        confirm_message = "Thanks for the message we will get back to you soon"
        form = None
    
    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'contact.html'
    return render(request,template,context)
