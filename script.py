#1/usr/bin/python
import MySQLdb as mdb

con = mdb.connect("localhost", "root", "Team4" ,"housesql");

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Testing1")
    cur.execute("CREATE TABLE Testing1(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Testing1(Name) VALUES('Jesse Zhou')")
    cur.execute("INSERT INTO Testing1(Name) VALUES('Honore de Balzac')")
    cur.execute("SELECT * FROM Testing1")

    rows = cur.fetchall()
    for row in rows:
        print row
