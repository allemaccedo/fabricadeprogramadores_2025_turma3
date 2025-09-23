from flask import Flask, request, jsonify, render_template, json
from main import ler_dados, autualizar_nota, criar_novo_usuario_e_nota, deletar_usuario
from tabelas import Usuario, Nota

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_data()
        usuario_e_nota = json.loads(data)

        user = Usuario(usuario_e_nota["usuario"],'email', 'senha')
        note = Nota(usuario_e_nota)
        criar_novo_usuario_e_nota(user, note)
        return jsonify({"msg": "Usuario e nota criados com sucesso!"})
    else:
        return jsonify({'error': 'Pagina nao encontrada!'}), 404
        
        
if __name__ == "__main__":
    app.run(debug=True)
