from fastapi.responses import JSONResponse
import pymysql
import pymysql.cursors
from db.db_mysql import get_db_connection


class empleadoService:
    def __init__(self):
        self.con= get_db_connection()
        if self.con is None:
            print("no se pudo establecer conexion")

    async def get_empleado(self):
         """inicializa la conexion"""
         try:
             self.con.ping(reconnect=True)
             with self.con.cursor(pymysql.cursors.DictCursor) as cursor:
                 sql="SELECT  e.id, e.nombre AS empleado_nombre, u.nombre AS usuario_nombre, u.apellido, u.numtelefono FROM empleado e  usuario u WHERE e.id = u.id"        

                 cursor.execute(sql)
                 empleado = cursor.fetchall()
                 if empleado:
                   return JSONResponse(content={
                     "success": True,
                      "data": empleado,
                       "massage":"empleado encontrado",
                      "status_code":200,
                   })

                 else:
                   return JSONResponse(content={
                     "success": False,
                     "massage":"empleado no encontrado",
                     "status_code":400,
                 } )
         except Exception as e:
                 return JSONResponse(content={
                     "success": False,
                     "massage":f"problemas al revisar empleado: {str(e)}",
                     "status_code":500,
                 })
