import sqlite3

conn = sqlite3.connect('mesa.db')
c = conn.cursor()


fd = open("./queries/select_run.sql", 'r')
sqlFile = fd.read()
fd.close()


result = c.execute("SELECT * FROM controls")

print(f"Resultado de la query: {result}")


conn.commit()
conn.close()