from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return jsonify({"message": "Este é um corpo (body) de uma requisição GET"})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "Esta é uma requisição POST!", "data": data})

if __name__ =='__main__':
    app.run(debug=True)