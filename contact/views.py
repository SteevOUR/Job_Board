from django.shortcuts import render

# Create your views here.
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


def send_message(request):

    infos = Info.objects.first()

    if request.method == 'POST':

        subject = request.POST['subject']
        message = request.POST['message']
        message += '\n\nName : ' + request.POST['name'] + "\nEmail From : < "
        message += request.POST['email'] + " > ."
        email = 'moustafa.ourahho@gmail.com'
        name = request.POST['name']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            name,
        )

        our_subject = 'MS_Support'
        our_message = 'We Have Been Received Your Request.\nAnd We Will Contact You As Soon As Possible.\n\nTeam MS_Developer.\nThank You ' + \
            request.POST['name'] + '.'
        email_dest = request.POST['email']

        send_mail(
            our_subject,
            our_message,
            settings.EMAIL_HOST_USER,
            [email_dest],
            name,
        )

    return render(request, 'contact/contact-us.html', {'infos': infos})
