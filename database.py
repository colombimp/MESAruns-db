import sqlite3
from unittest import result

# creamos la DB en el archivo mesa.db
conn = sqlite3.connect('mesa.db')

# creamos un cursor: con esto nos conectamos a la DB
c = conn.cursor()

# creamos una tabla ejecutando un comando SQLite. OJO: es case sensitive
c.execute("""CREATE TABLE mesaruns (
    run_id INTEGER
)
""")

# lo que necesites poner True or False ponelo como un entero 1 (True) o 0 (False)
c.execute("""CREATE TABLE controls (
    MESArun INTEGER,
    alpha_semiconvection REAL,
    log_directory TEXT,
    thermohaline_coeff REAL,
    use_Ledoux_criterion INTEGER,
    use_other_wind INTEGER
    )""")

# agregamos una fila de datos en la tabla controls

c.execute("""INSERT INTO controls VALUES (
    0,
    1.1,
    'LOGS1',
    1.2,
    1,
    1
)
""")

# Si queremos agregar de a mas de una fila, tiene que ser a partir de una lista con tuplas:
inputs = [
    (1,1.1,'LOGS2',1.2,1,1),
    (2,2.0,'LOGS1',1.3,0,0),
    ]
# y el comando es execute many
c.executemany("INSERT INTO controls VALUES (?, ?, ?, ?, ?, ?)", inputs)

# para ver los resultados hacemos un SELECT * (seleccionamos todas las entradas)
c.execute("SELECT * FROM controls")
# y un fetchall para que nos muestre TODO (CUIDADO) cuando corramos el script. el resultado es una tupla

results = c.fetchall()
print(results)

# ponele que quiero hacer algo con los resultados:


print(f"parametros de la corrida {results[0][0]}: {results[0][1:]}")
# guardamos todo en la DB
conn.commit()


#cerramos la conexion
conn.close()