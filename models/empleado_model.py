from typing import Union
from pydantic import BaseModel

from models.user_model import User


class empleado(BaseModel):
    nombre:str
    edad:str
    direccion:str
    usuario: Union[int, User]
