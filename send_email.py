import smtplib
import ssl
import os

def send_mail(message):
    global server
    host = "smtp.gmail.com"
    port = 465

    username = "sumitasranicoder@gmail.com"
    password = os.getenv("Password")

    receiver = "sumitasranicoder@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


