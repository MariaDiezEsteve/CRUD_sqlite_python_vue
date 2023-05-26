#Para utilizar la librería de sqlite3 tenemos que importar el módulo

import sqlite3

from estudiantes import Estudiante

#1. Conexión con la BBDD: universidad.db
#Si no existe al BBDD crea un archivo.
con = sqlite3.connect("universidad.db")
#Terminal: python sqlite.py

#3.Crear un objeto cursor para hacer peticiones(querys)= consulta a la BBDD(sqlite3)
#cursor() = Se utiliza para hacer peticiones
cu = con.cursor()

#4. 1º Consulta: Crear una tabla -> En los parámetros ponemos la consulta que queremos hacer. Utilizamos  triple comillas porque va a ser un string párrafo.

#execute() sirve para manipular la BBDD de sqlite, solo escribe

cu.execute(""" CREATE TABLE IF NOT EXISTS estudiantes (
                matricula TEXT PRIMARY KEY,
                nombre TEXT,
                apellido TEXT,
                promedio REAL)            
            """)

#Si la tabla existe no la crea

#5. 2º Consulta: Insertar los datos de la tabla 

cu.execute(""" INSERT INTO estudiantes VALUES("116", "Eiii", "Diez", 4) """)

#Otra manera de insertar datos en una tabla con variables:
est_1 = Estudiante("222", "María", "Esteve", 10)

#commmit = guarda la petición en la BBDD "la crea"
con.commit()

#6. 3º Consulta: Seleccionar todos los estudiantes que están en mi BBDD
#* Selecciona todas las propiedades (matricula, nombre, apellido, promedio)
cu.execute("SELECT  * FROM estudiantes")

#Le asignamos a una variable toda la BBDD de la petición
#fetchall: nos devuelve todos los estudiantes
estudiantes = cu.fetchall()
print(estudiantes) #[('111', 'María', 'Diez', 9.5), ('112', 'Diez', 'Esteve', 9.5)] te devuelve una lista

#fetchmany(numero): cuantos estudiantes queremos que nos devuelva, y nos lo devuelve
estudiantes = cu.fetchmany(5)
print(estudiantes)


#Cerra la BBDD
con.close()