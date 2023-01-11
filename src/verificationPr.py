import sqlite3 
import getpass
import sys

def main():
    crear_usuario(5, 'admin', 'user2')

def main2():
    username = input("Nombre de usuario:")
    password = getpass.getpass("Contraseña: ")
    
    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto+")

def verifica_credenciales(username,password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    
    identificador += 1
    query = f"SELECT id FROM user WHERE username = '{username}' AND password = '{password}'"
    
    print(f"Query a ejecutar: {query}")
    rows = cursor.execute(query)
    data = rows.fetchone()
    
    cursor.close()
    conn.close() 
    # print(f"Data es {type(data)}")

    
    # row = cursor.execute(
    #     f"SELECT id FROM user WHERE username = {username} AND password = {password}"
    #     )
    
 
def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db') #, isolation_level=None
    cursor = conn.cursor()
    
    query = f"INSERT INTO user (id, username, password) VALUES(?,?, ?)"
    
    rows = cursor.execute(query, (identificador, usuario, clave))
    print(type(rows))
    conn.commit()
    data = rows.fetchone()
    cursor.close()
    conn.close()  
    
    

    
 
        

if __name__ == '__main__':
    main()
    
sys.exit(0)

conn = sqlite3.connect('miaplicacion.db')

cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM user WHERE username = "Tony"')

for row in rows:
    print(row)

cursor.close()

conn.close()