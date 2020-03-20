from dataclasses import dataclass, field
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Tuple


@dataclass
class EmailModelo:
    de: str
    contrasenia: str
    para: List[str]
    encabezado: str
    cuerpo: str = ''
    copia: List[str] = field(default_factory=list)
    adjuntos: List[Tuple[str, bytes]] = field(default_factory=list)

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
        return EmailModelo(**d)
