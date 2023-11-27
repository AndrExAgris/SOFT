from flask import Flask, render_template, request, redirect, url_for, session
from src.negocio.gerenciador_tarefas import GerenciadorTarefas
from src.negocio.notificacoes import socketio, configurar_socketio
from src.negocio.relatorios import Relatorios
from src.dados.usuario import Usuario
app = Flask(__name__)

users = [Usuario]

gerenciador_tarefas = GerenciadorTarefas()
relatorios = Relatorios(gerenciador_tarefas)

# Adicione mais rotas conforme necessário
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username and password match
        if username in users and users[username] == password:
            session['username'] = username  # Store the username in the session
            return redirect(url_for('home'))

        # If the login is unsuccessful, show an error message
        error = 'Invalid username or password. Please try again.'
        return render_template('login.html', error=error)

    return render_template('login.html')
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
