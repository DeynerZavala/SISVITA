import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os


load_dotenv()


def cargar_configuracion_email():
   configuracion = {
       'servidor_smtp': os.getenv('SMTP_SERVER'),
       'puerto_smtp': os.getenv('SMTP_PORT'),
       'usuario': os.getenv('SMTP_USER'),
       'contrasena': os.getenv('SMTP_PASSWORD'),
   }


   # Verificar que todas las variables de entorno se hayan cargado correctamente
   for key, value in configuracion.items():
       if value is None:
           raise ValueError(f"La variable de entorno {key} no está definida en el archivo .env")


   return configuracion


def enviar_correo_diagnostico(usuario, especialista_id, fecha, tratamiento_id, solicitar_cita):
   config = cargar_configuracion_email()
   destinatario = usuario.correo_electronico
   asunto = "Resultado de tu examen"
   cuerpo = f"Estimado/a {usuario.nombre},\n\nHemos terminado de corregir tu examen.\n\n" \
            f"Especialista: {especialista_id}\n" \
            f"Fecha: {fecha}\n" \
            f"Tratamiento: {tratamiento_id}\n\n"


   if solicitar_cita:
       cuerpo += f"Además, se ha solicitado una cita. Aquí tienes los detalles:\n\n"


   cuerpo += "Atentamente,\nEl equipo de Sisvita."


   msg = EmailMessage()
   msg['From'] = config['usuario']
   msg['To'] = destinatario
   msg['Subject'] = asunto
   msg.set_content(cuerpo)


   context = ssl.create_default_context()


   try:
       with smtplib.SMTP_SSL(config['servidor_smtp'], int(config['puerto_smtp']), context=context) as server:
           print("Conectando al servidor SMTP...")
           server.login(config['usuario'], config['contrasena'])
           print("Iniciado sesión en el servidor SMTP.")
           server.sendmail(config['usuario'], destinatario, msg.as_string())
           print(f"Correo enviado exitosamente a {destinatario}.")
   except Exception as e:
       print(f"Error al enviar el correo: {e}")