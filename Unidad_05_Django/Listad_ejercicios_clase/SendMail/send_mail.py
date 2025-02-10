import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SendMail.settings")
django.setup()

import smtplib, ssl

from clientes.models import Cliente

# Buscar a un cliente
cliente = Cliente.objects.get(pk=6)
print(cliente)

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "jrodri77@educarex.es"
password = input("Type your password and press enter: ")

#  to
receiver_email = "jrodri77@educarex.es"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, "Subject: Prueba de correo\n\nEste es un correo de prueba")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 