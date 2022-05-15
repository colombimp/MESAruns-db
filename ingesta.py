import sqlite3

# para ingestar las namelists:
# Lo que me imagino es importar la clase que levante las namelists de fortran
# y una vez generado cada diccionario, guardarlo en la db


def generate_dict(*args, **kwargs): # esto lo harias con la clase no?
    data_dict = { # a modo de ejemplo
        "controls": {
            "alpha_semiconvection": 1.0,
            "log_directory": "LOGS1",
            "thermohaline_coeff": 1.0,
            "use_Ledoux_criterion": True,
            "use_other_wind": True,
        },
        "eos": {},
        "kap": {
            "Zbase": 0.02,
        },
        "pgstar": {},
        "star_job": {
            "change_rotation_flag": True,
            "new_rotation_flag": True,
            "new_surface_rotation_v": 10,
            "show_log_description_at_start": False
        }
    }
    return data_dict


# def nl_to_db(dictionary, **kwargs):
#     conn = sqlite3.connect('mesa.db')
#     c = conn.cursor()
#     for key in dictionary.keys(): #cada key del dict original es una tabla de nuestra DB
#         table_name = key.lower()

#         stat = f"INSERT INTO {table_name} VALUES " # MUCHO CUIDADO ACA con el nombre de la tabla
#         n_values = "(" + "?, "*(len(dictionary.keys())-1) + " ?)"

#         values = dictionary[key].values()

#         c.execute(stat + n_values, values) #inserto los datos en la tabla

#     # guardamos todo en la DB
#     conn.commit()

#     #cerramos la conexion
#     conn.close()