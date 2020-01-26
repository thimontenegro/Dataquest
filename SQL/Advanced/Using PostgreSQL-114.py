## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('CREATE TABLE notes ( id INTEGER PRIMARY KEY, body TEXT, title TEXT);')
cur.close()

## 5. SQL Transactions ##

conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
conn.commit()
conn.close()


## 6. Autocommitting ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect('dbname= dq user=dq')
cur = conn.cursor()
conn.commit()
cur.execute('SELECT * FROM notes;')
rows = cur.fetchall()
print(rows)
conn.close()
 

## 8. Creating a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('CREATE DATABASE income OWNER dq')
conn.close()


## 9. Deleting a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('DROP DATABASE income')
conn.close()
