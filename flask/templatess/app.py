from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return '<h1>Bem-Vindo à Home!</h1>'

def valid_login(username, password):
    return username == "admin" and password == "123"

def log_the_user_in(username):
    return f"<h2>Bem-vindo, {username}!</h2>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Usuário ou senha inválidos'
    return render_template('login.html', error=error)

@app.route('/sobre/<num>')
def sobre(num):
    return render_template('index.html', numero=num)

if __name__ == '_main_':
    app.run(debug=True)