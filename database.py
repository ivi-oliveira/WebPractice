import mysql.connector

def conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3310,
        database="cadastro"
        )
