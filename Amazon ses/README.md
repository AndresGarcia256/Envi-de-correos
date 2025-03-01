# Envio de correos con Amazon ses
Este repositorio tiene como proyecto enviar un correo por medio de amazon ses, Amazon ses fue hecho principalmente para enviar correos de forma masiva de productos de sus clientes o productos propios.

Este servicio de amazon permite primero enviar correos a correos verificados en la misma cuenta de amazon, para poder enviar correos a correos no verificados se tendra que hablar con amazon para ponerlo en produccion y de esta manera poder enviar cientos de correos a cualquier destinatario.

# Credenciales de Amazon 
Tendra dos formas de añadir sus credenciales.
# Añadir en forma de variable (No recomendada por temas de seguridad)
```
ses_client = boto3.client('ses' , region_name = 'tu-region' , aws_access_key_id = 'tu-access-key-id' , aws_secret_access_key = 'tu-secret-access-key')
```
# Añadir como variable de entorno (Recomendado por temas de seguridad)
Tendra que instalar la libreria donatev para llamar las variables que guardara en un archivo .env
```
pip install python-dotenv
```
Debera tener en su directorio o carpeta un archivo llamado .env donde podra guardar las variables de esta manera.
```
AWS_ACCESS_KEY_ID=tu-access-key-id
AWS_SECRET_ACCESS_KEY=tu-secret-access-key
AWS_DEFAULT_REGION=tu-region
```
En el codigo de python usara este codigo para llamar las variables 
```
ses_client = boto3.client('ses' , region_name = os.getenv('AWS_DEFAULT_REGION') , aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID') , aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'))
```
# Enviar correo
Ahora para enviar el correo tendra que tener en cuenta varias secciones importantes como lo son Sender, Recipient y Subjet
```
SENDER = "Remitente"  # Reemplaza con tu correo verificado en SES
RECIPIENT = "Destino"  # Reemplaza con el correo del destinatario, En caso de necesitar enviar a mas destinatarios, separarlos por comas
SUBJECT = "Asunto del correo" # Asunto del correo
```
La manera en la que quiera enviar el correo sera importante si lo requiere como un texto plano o si lo requiere como html para mayor personalizacion, eso lo podra escoger de manera que se use body_text y body_html
```
BODY_TEXT = "Este es el contenido del correo en texto plano."
BODY_HTML = """
<html>
<head></head>
<body>
  <h1>Hola!</h1>
  <p>Este es el contenido del correo en <b>HTML</b>.</p>
</body>
</html>
"""
CHARSET = "UTF-8"
```
Por ultimo usara un try para enviar el correo por medio del send_mail y se verificara que las credenciales esten correctas.
```
try:
    response = ses_client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
except (NoCredentialsError, PartialCredentialsError) as e:
    print("Error de credenciales:", e)
except Exception as e:
    print("Error enviando correo:", e)
else:
    print("Correo enviado:", response['MessageId'])


```









