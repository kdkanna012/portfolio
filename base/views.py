from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    return render(request, 'index.html')


def send_email(request):

    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name': request.POST['sender-name'],
            'email': request.POST['sender-email'],
            'message': request.POST['message']
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['kannadasan1931@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'email_sent.html')
