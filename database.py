import sqlite3

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
    mesarun INTEGER,
    alpha_semiconvection REAL,
    log_directory TEXT,
    thermohaline_coeff REAL,
    use_Ledoux_criterion INTEGER,
    use_other_wind INTEGER
    )""")


# guardamos todo en la DB
conn.commit()

#cerramos la conexion
conn.close()