import sqlite3




def crear_tabla_puntajes():

    with sqlite3.connect("bd_juego.db") as conexion:
        try:
            sentencia = ''' create table puntajes
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntajes")  

        except sqlite3.OperationalError:

            print("La tabla puntajes ya existe")


def insertar_puntajes(nombre, puntaje)->None:

    with sqlite3.connect("bd_juego.db") as conexion:  

        try:
            conexion.execute("insert into puntajes(nombre,puntaje) values (?,?)", (nombre, puntaje)) 
            conexion.commit()

        except:
            print("Error")


def obtener_datos():

    with sqlite3.connect("bd_juego.db") as conexion:

        try:
            cursor = conexion.execute("select * from puntajes order by puntaje desc limit 5")
            lista = cursor.fetchall()
            print(lista)
        except:
            print("Error de registros")
            lista = []

        return lista

