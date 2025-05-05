
from fastapi import APIRouter
from models.venta_model import venta
from models.empleado_model import empleado
from sevices import user_service
from sevices import empleado_service
from sevices.empleado_service import empleadoService
from sevices.user_service import UserService
from models.user_model import User
from sevices.venta_sevice import ventaService



routes=APIRouter(prefix="/user", tags=["Users"])
routes_e=APIRouter(prefix="/empleado", tags=["empleado"])
routes_v=APIRouter(prefix="/venta", tags=["venta"])

user_service = UserService()
user_model=User
empleado_service=empleadoService()
empleado_model=empleado
venta_service=ventaService()
venta_model=venta



@routes.get("/get-users/")
async def get_all_users():
    result=await user_service.get_users()
    return result


@routes.get("/get-users/{user_id}")
async def get_user(user_id: int):
    return await user_service.get_user_by_id(user_id)

#Modelo para crear rutas, crear una para cada método
@routes.post("/nombre-metodo/") 
async def nombre_metodo():
    return "Nombre método"
   
@routes.post("/create-user/")
async def create_user(user: User):
    return await user_service.create_users(user)

@routes.patch("/change-password/")
async def change_password(id: str, new_password: str):
    return await user_service.change_password(id, new_password)

@routes.patch("/inactivate/{user_id}")
async def inactivate_user(user_id: int):
    return await user_service.inactivate_user(user_id)

@routes.patch("/change-status/{user_id}")
async def change_user_status(user_id: int):
    return await user_service.toggle_user_status(user_id)

@routes.put("/update-user/{user_id}")

async def update_user(user_id: int, user_data: User):
    return await user_service.update_user(user_id, user_data)

@routes_e.get("/get-empleado/")
async def get_all_empleado():
    return await empleado_service.get_empleado()

@routes_e.get("/get-empleado/{id_empleado}")
async def get_empleado(id_empleado: str):
    return await empleado_service.get_empleado(id_empleado)

@routes_e.post("/create-empleado/")
async def create_empleado(empleado: empleado):
    return await empleado_service.create_empleado(empleado)

@routes.patch("/change-empleado/")
async def change_empleado(id: str, new_empleado: str):
    return await empleado_service.change_empleado(id, new_empleado)

@routes.patch("/inactivate/{empleado_id}")
async def inactivate_empleado(empleado_id: str):
    return await empleado_service.inactivate_empleado(empleado_id)

@routes.patch("/change-status/{empleado_id}")
async def change_empleado_status(empleado_id: str):
    return await empleado_service.toggle_empleado_status(empleado_id)

@routes.put("/update-empleado/{empleado_id}")

async def update_empleado(empleado_id: int, empleado_data: empleado):
    return await empleado_service.update_empleado(empleado_id, empleado_data)


