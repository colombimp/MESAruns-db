import sqlite3

def create_db(db_name: str, data_dict):
    # creamos la DB
    conn = sqlite3.connect(db_name+".db")
    c = conn.cursor()

    dtype_map = { # conversion de dtypes de python a sqlite
        None: "NULL",
        int: "INTEGER",
        float: "REAL",
        str: "TEXT",
        bytes: "BLOB",
        bool: "INTEGER",
        }

    for table_name, table_values in data_dict.items():
        command = f"CREATE TABLE {table_name.lower()} ( "
        for key, value in table_values.items():
            command += str(key) + " " + dtype_map[type(value)] + ", "  # TODO: revisar los datatypes, de ultima hardcodear
        command += ");"
        #print(command)
        c.execute(command)
    # guardamos todo en la DB
    conn.commit()

    #cerramos la conexion
    conn.close()

