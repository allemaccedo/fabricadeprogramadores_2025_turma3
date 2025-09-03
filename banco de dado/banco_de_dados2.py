import sqlite3
try:
    con = sqlite3.connect("segundo_banco.db")
    cur = con.cursor()

    #cur.execute("DROP TABLE pessoa")

    cur.execute("CREATE TABLE pessoa(" +
                "id_pessoa INTEGER PRIMARY KEY ASC AUTOINCREMENT," +
                "nome VARCHAR(400)," +
                "idade INTEGER," +
                "cpf VARCHAR(15))")

    cur.execute("CREATE TABLE consulta(" +
                "id INTEGER PRIMARY KEY ASC AUTOINCREMENT," +
                "data_consulta DATETIME," +
                "horario DATETIME," +
                "id_pessoa INTEGER," +
                "FOREIGN KEY (id_pessoa) REFERENCES pessoa(id_pessoa))"
                )

    cur.execute("SELECT * FROM pessoa, data_consulta FROM pessoa, consulta WHERE pessoa.id_pessoa = %d" % 1)
    res = cur.fetchone()
    print(res)

    con.commit()
    cur.close()
    con.close()
except ConnectionRefusedError as c:
    print('Erro de Conexão:', c)