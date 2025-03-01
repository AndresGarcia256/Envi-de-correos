import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

correo = os.getenv('Correo')
Contrasena = os.getenv('Contrasena')

destinatario = "Destino"
mensaje = "Hola mundo "
email = EmailMessage()
email["From"] = correo
email["To"] = destinatario  
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)


smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(correo, Contrasena)
smtp.sendmail(correo, destinatario, email.as_string())
smtp.quit()
