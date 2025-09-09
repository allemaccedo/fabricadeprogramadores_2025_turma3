import sqlite3
try: 
 con = sqlite3.connect("chaves.db")
 cur = con.cursor()

 cur.execute("CREATE TABLE chaves(id,nome,sala_correspondente)")

 cur.execute("INSERT INTO chaves VALUES(1,'Ana','Recepção')") 
 cur.execute("INSERT INTO chaves VALUES(2,'Bruno', 'Financeiro')") 
 cur.execute("INSERT INTO chaves VALUES(3,'Carla', 'Depósito')") 

 cur.execute("SELECT nome FROM chaves WHERE sala_correspondente = 'Financeiro'")
 resultado = cur.fetchone()

 if resultado:
    print(f"Quem está com a chave do Depósito é: {resultado[0]}")
 else:
    print("Ninguém está com a chave do Depósito.")

 cur.close()
 con.commit()

except ConnectionResetError as c:
 print ('Erro de conexão com o banco.')