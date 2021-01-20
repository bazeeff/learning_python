import sqlite3 as sql

conn = sql.connect('database.db')
curs = conn.cursor()

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

curs.execute('SELECT * FROM zoo')

rows = curs.fetchall()
print(rows)
curs.close()
conn.close()