# Base de datos 
# organizda de inforación, que se encuentra estrutura y almecana de una computadora
# Las DB se clasifican generalmente en dos clases, relaciones y no relacionales

# DB SQL
# Datos que se relacionan entre si y tienen "id"

#DV NoSQL
#  NO relacionales corresponden a esquemas flexibles, especialmente utilizados cuando se requier manejar un grnade valomun de datos y baja latencia FORMATO JSPON 

#SENTENCIAS
# el fundamento general consulta o recuperacion o madoficar elementos 

# LENGUAJE DE DEFINICON DE DATOS:
# Create: sirve para crear una  DB, tables
# alter: sirve para modificar la estructura, aladiendo o  borrando columnas
# DROP: sirve para elimiar objetos de la esturtura, de una o en secuencial

#LENGUAA DE MANIPULACION DE DATOS:
# select  realizar consulta 
# insert insetatr valores
# update modifica valores 
# delete para eliminar las filas de una tablas

#LENGUJA DE CONTROL DE DATOS
# grant otorga acceso de usuario
# revoke retirir privilegios 
import sqlite3
def Registrar(nombre,apellido,documento):
    db=sqlite3.connect("MateoDB.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="Insert into Programas (nombre,apellido,documento))\
        valus('"+ nombre+"','"+apellido+"',"\
            +str(documento)+")"
    cursor.execute(consulta)
    db.commit()
    cursor.close()
    db.close()
if __name__=='__main__':
    Registrar('Mateo','Nossa',1032936230)