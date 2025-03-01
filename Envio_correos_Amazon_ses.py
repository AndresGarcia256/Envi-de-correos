import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

#Credenciales de amazon aw
"""
En una terminal Bash se pueden agregar las credenciales, boto3 las tomara del entorno con este codigo se podran agregar las credenciales 
export AWS_ACCESS_KEY_ID='tu-access-key-id'
export AWS_SECRET_ACCESS_KEY='tu-secret-access-key'
export AWS_DEFAULT_REGION='tu-region'
En caso de 
"""

# Configuración de SES
ses_client = boto3.client('ses', region_name='Region') # Region y servicio que se necesita

# Parámetros del correo
SENDER = "Remitente"  # Reemplaza con tu correo verificado en SES
RECIPIENT = "Destino"  # Reemplaza con el correo del destinatario, En caso de necesitar enviar a mas destinatarios, separarlos por comas
SUBJECT = "Asunto del correo"
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