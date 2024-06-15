from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):

  subject = "Hello, is Jorghee"
  message = "I am programmer, I like the apples and penguins"
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ['mamannihuarsaya4b@gmail.com']

  report = "Correo enviado exitosamente"
  try:
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
  except Exception as e:
    report = "Error al enviar el correo"
    print(e)

  return render(request, 'send/index.html', { "report":report })
