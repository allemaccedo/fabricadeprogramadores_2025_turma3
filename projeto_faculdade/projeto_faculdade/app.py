from flask import Flask, request, jsonify, render_template, json, redirect, url_for
from main import ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario, login_de_usuario,  matricular_aluno
from tabelas import Usuario, Nota, joinedload

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_data()
        usuario_o_nota = json.loads(data)

        user = Usuario(
                        nome = usuario_o_nota["usuario"], 
                        email =usuario_o_nota["email"] ,
                        senha_hash = usuario_o_nota["senha"] )

        note = Nota(
                    titulo = usuario_o_nota["titulo"],
                    conteudo = usuario_o_nota ["nota"])

        criar_novo_usuario_e_nota(user, note)
        return jsonify ({"message": "Usuário e nota criados com sucesso!"}), 201
    else:
        return jsonify({'error': 'Página não encontrada!'}), 404

@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        data = ler_dados()
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"sucess": False, "error": str(e)}), 500


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_data()
        usuario = json.loads(data)
        user = Usuario(email=usuario["email"], senha_hash=usuario["senha_hash"])
        print('usuario', user)
        try:
            usr = login_de_usuario(user)
            app.logger.info("Usuário de email: %s logado!" % usuario["email"])
            return redirect(url_for("home", data=usr))
        except Exception as e:
            app.logger.error("Erro no servidor: ", str(e))
            return jsonify({"success": False, "error": str(e)}), 500
    else:
        return render_template('login.html')

@app.route("/remover/usuarios/<id_usuario>", methods=["GET", "POST"])
def remover_usuarios(id_usuario):
    if request.method == "POST":
        data = request.get_data()
        id_usuario = json.loads(data)
        try:
            deletar_usuario(id_usuario=id_usuario)
            app.logger.info("usuario do id: %d foi removido com sucesso")
            return redirect(url_for("index"))
        except Exception as e:
            app.logger.error("Erro na remoção de usuarios:", str(e))
            return jsonify({"success": False, "error": str(e)}),500
    else:
            return render_template('remover.html')

@app.route("/matricula/<id_usuario>/<id_curso>", methods=['GET', 'POST'])
def matricula(id_usuario, id_curso):
    if request.method == "POST":
        data = request.get_data()
        ids = json.loads(data)
        try:
            matricular_aluno(ids['id_usuario'],ids['id_curso'])
            app.logger.info("Usuario do id: %s foi matriculado!" % ids['id_usuario'])
            return redirect(url_for('home'))
        except Exception as e:
            app.logger.error("Erro na Matricula de usuário: ", str(e))
            return jsonify({"sucess": False, "error": str (e)}), 500
    else:
         return render_template('matricula.html')
    
if __name__ == "__main__":
    app.run()