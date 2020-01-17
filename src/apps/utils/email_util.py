import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apps.models.emails import EmailModelo
from typing import List, Tuple

_SMT_HOST = 'smtp.gmail.com'
_SMT_PORT = 465


def enviar_email(email_a_enviar: EmailModelo):
    '''
    Envia el email
    '''
    text = _preparar_email(email_a_enviar)
    context = ssl.create_default_context()

    receiver_email = EmailModelo.lista_a_str(email_a_enviar.para)

    server = smtplib.SMTP_SSL(_SMT_HOST, _SMT_PORT, context=context)
    server.login(email_a_enviar.de, email_a_enviar.contrasenia)
    server.sendmail(email_a_enviar.de, receiver_email, text)


def _preparar_email(email_a_enviar: EmailModelo) -> str:
    '''
    Preparar email para el enviador de email
    '''
    message = MIMEMultipart()
    message["From"] = email_a_enviar.de
    message["To"] = EmailModelo.lista_a_str(email_a_enviar.para)
    message["Subject"] = email_a_enviar.encabezado
    message["Bcc"] = EmailModelo.lista_a_str(email_a_enviar.copia)
    message.attach(MIMEText(email_a_enviar.cuerpo, "plain"))

    for part in _preparar_adjuntos(email_a_enviar.adjuntos):
        message.attach(part)

    return message.as_string()


def _preparar_adjuntos(adjuntos: List[Tuple[str, bytes]]) -> List[MIMEBase]:
    '''
    Prepara los adjuntos para el enviador de emails
    '''
    resultado = []
    for adjunto in adjuntos:

        nombre = adjunto[0]
        contenido = adjunto[1]

        part = MIMEBase("application", "octet-stream")
        part.set_payload(contenido)

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {nombre}",
        )

        resultado.append(part)

    return resultado