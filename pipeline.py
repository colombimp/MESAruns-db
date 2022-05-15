import ingesta
import database

ex_dict = ingesta.generate_dict()

# Primero creamos la database
c = database.create_db("mesa", ex_dict)
