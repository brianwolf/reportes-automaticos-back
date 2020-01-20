from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Tuple


class EmailModelo(object):
    def __init__(self,
                 de: str,
                 contrasenia: str,
                 para: List[str],
                 encabezado: str,
                 cuerpo: str = '',
                 copia: List[str] = '',
                 adjuntos: List[Tuple[str, bytes]] = []):
        self.de = de
        self.contrasenia = contrasenia
        self.para = para
        self.encabezado = encabezado
        self.cuerpo = cuerpo
        self.copia = copia
        self.adjuntos = adjuntos

    def to_dict(self):
        return {
            'de': self.de,
            'contrasenia': self.contrasenia,
            'para': self.para,
            'cuerpo': self.cuerpo,
            'encabezado': self.encabezado,
            'copia': self.copia,
            'adjuntos': self.adjuntos
        }

    @staticmethod
    def from_dict(d: dict):
        return Email(**d)