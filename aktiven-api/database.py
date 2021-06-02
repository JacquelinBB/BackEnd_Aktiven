import sqlite3

conn = sqlite3.connect('database.sqlite')

cursor = conn.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, usuario text, senha integer)")
sql_query = """ CREATE TABLE pessoas (
    id integer PRIMARY KEY,
    nome text NOT NULL,
    nome_robo text NOT NULL,
    usuario text NOT NULL,
    senha integer NOT NULL,
    resenha integer NOT NULL
)"""
cursor.execute(sql_query)

#cursor.execute("INSERT INTO pessoas VALUES('1','Maria','Maria72','547965Mar*')")
conn.commit()
#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

