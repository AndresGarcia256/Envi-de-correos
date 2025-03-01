import smtplib
from email.message import EmailMessage

remitente = "Remitente"
destinatario = "Destino"
mensaje = "Hola mundo "
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario  
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(remitente, "Contraseña")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()
print("correo enviado")