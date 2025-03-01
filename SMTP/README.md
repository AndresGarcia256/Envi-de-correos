# Envio de Correos por SMTP
Para enviar correos por medio de SMTP se requiere el correo y constraseña del correo o contraseña de hardware para poder ingresar al correo
# Uso de credenciales del correo
El uso correcto para añadir y usar el correo y clave correcta tendra que añadir un archivo llamado .env
En el archivo .env podra correo y contraseña
```
Correo=tu-correo
Contrasena=tu-contraseña
```
Luego tendra que instalar la libreria donatev
```
pip install python-dotenv
```
Ahora podra llamar las variables de esta manera
```
correo = os.getenv('Correo')
Contrasena = os.getenv('Contrasena')
```
Luego de tener estas variables podra comenzar a usar el codigo
# Enviar correo
Tendremos primero esta seccion donde podra escoger el correo destino y luego podra armar el email como sera From = Su correo, To = destino, Subjet = Asunto y mensaje
```
destinatario = "Destino"
mensaje = "Hola mundo "
email = EmailMessage()
email["From"] = correo
email["To"] = destinatario  
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
```
Luego tendremos estsa seccion donde se iniciara el protocolo smtp donde se podra escoger el puerto 587 y escogera outlook o gmail o el que necesite que podra buscarlo en la pagina oficial de su proveedor de correo electronico
```
smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(correo, Contrasena)
smtp.sendmail(correo, destinatario, email.as_string())
smtp.quit()
```




