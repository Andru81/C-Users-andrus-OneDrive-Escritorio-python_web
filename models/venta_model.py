from typing import Union
from pydantic import BaseModel

from models.user_model import User


class venta(BaseModel):
    fecha_venta:int
    hora_venta:int
    total:int
    usuario: Union[int, User]
