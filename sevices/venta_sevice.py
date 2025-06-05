from fastapi.responses import JSONResponse
import pymysql
import pymysql.cursors
from db.db_mysql import get_db_connection
from models.venta_model import venta


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
                 sql="SELECT v.id, v.total, v.hora_venta, v.fecha_venta, u.nombre, u.apellido FROM venta v JOIN usuario u ON v.usuario_FK=u.id"

                 cursor.execute(sql)
                 venta = cursor.fetchall()
                  
                 return JSONResponse(content={
                     "success": True,
                      "data": venta,
                       "massage":"venta encontradas",
                      "status_code":200,
                 })
                
         except Exception as e:
                 return JSONResponse(content={
                     "success": False,
                     "massage":f"problemas al revisar venta: {str(e)}",
                     "status_code":500,
                 })

     async def create_venta(self, venta_data: venta):
        """Crea un nuevo u en la base de datos y devuelve una respuesta estructurada."""
        try:
             self.con.ping(reconnect=True)
             with self.con.cursor() as cursor:
                # Verificar si la venta ya existe
                check_sql = "SELECT COUNT(*) FROM venta WHERE usuario = %s"
                cursor.execute(check_sql, (venta_data.usuario,))
                result = cursor.fetchone()
                
                if result[0] > 0:
                    return JSONResponse(
                        status_code=400,
                        content={"success": False, "message": "la venta ya ese encuenra registrado", "data": None}
                    )
                             
        except Exception as e:
                 return JSONResponse(content={
                     "success": False,
                     "massage":f"problemas al revisar venta: {str(e)}",
                     "status_code":500,         
                 })