from dataclasses import dataclass
from copy import deepcopy


@dataclass
class AppModel:
    def to_dict(self):

        self_dict = deepcopy(self.__dict__)

        for key, value in self.__dict__.items():

            if hasattr(value.__class__, 'to_dict'):
                self_dict[key] = value.to_dict()

        for attrname in dir(self.__class__):
            if isinstance(getattr(self.__class__, attrname), property):
                self_dict[attrname] = getattr(self, attrname)

        return self_dict


@dataclass
class Mascota(AppModel):
    nombre: str

    __attr_class = [str, int]


@dataclass
class Persona(AppModel):
    nombre: str
    edad: int
    mascota: Mascota

    @property
    def esta_vivo(self) -> bool:
        return True


@dataclass
class Alumno(Persona):
    legajo: str


yo = Alumno(legajo='1496414',
            nombre='brian',
            edad=26,
            mascota=Mascota('Terry'))

# print(yo.__dict__)
# print(yo.to_dict())
# print(yo.__dict__)

print(Mascota.__attr_class)
