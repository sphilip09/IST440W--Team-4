import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'Team4', 'housesql');

with con:

        cur = con.cursor()

        cur.execute("DELETE FROM Testing1 WHERE Name = 'Honore de Balzac'")

        print "Number or rows deleted:", cur.rowcount

        rows = cur.fetchall()
        for row in rows:
                print row
