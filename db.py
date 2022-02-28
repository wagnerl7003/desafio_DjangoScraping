import sqlite3

from numpy import insert

banco = sqlite3.connect('db.sqlite3')

cursor = banco.cursor()

def InsertSqlite(myvalue):
    cursor.execute("INSERT INTO app_proxylist (ip_address, port, protocol, anonymity, country, region, city, uptime, response, transfer)  VALUES("+ myvalue +")")

    banco.commit()

def SelectSqlite():
    cursor.execute("SELECT * FROM app_proxylist")
    print(cursor.fetchall())

def DeleteSqlite():
    cursor.execute("DELETE FROM app_proxylist")
    banco.commit()


# DeleteSqlite()
