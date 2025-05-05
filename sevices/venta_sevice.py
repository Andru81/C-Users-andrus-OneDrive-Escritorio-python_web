from fastapi.responses import JSONResponse
import pymysql
import pymysql.cursors
from db.db_mysql import get_db_connection


class ventaService:
     def __init__(self):
        self.con= get_db_connection()
        if self.con is None:
            print("no se pudo establecer conexion")

     async def get_venta(self):
         """inicializa la conexion"""
         try:
             self.con.ping(reconnect=True)
             with self.con.cursor(pymysql.cursors.DictCursor) as cursor:
                 sql="SELECT v.id, v.total, u.nombre, u.apellido, u.numtelefono FROM venta v JOIN usuario u ON v.usuario=u.id"

                 cursor.execute(sql)
                 venta = cursor.fetchall()
                 if venta:
                   return JSONResponse(content={
                     "success": True,
                      "data": venta,
                       "massage":"venta encontradas",
                      "status_code":200,
                 })
                 else:
                   return JSONResponse(content={
                     "success": False,
                     "massage":"venta no encontradas",
                     "status_code":400,
                 } )
         except Exception as e:
                 return JSONResponse(content={
                     "success": False,
                     "massage":f"problemas al revisar venta: {str(e)}",
                     "status_code":500,
                 })

                 
                 
