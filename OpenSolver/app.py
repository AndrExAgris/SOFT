from flask import Flask, render_template
from src.negocio.gerenciador_tarefas import GerenciadorTarefas
from src.negocio.notificacoes import socketio, configurar_socketio
from src.negocio.relatorios import Relatorios

app = Flask(__name__)

gerenciador_tarefas = GerenciadorTarefas()
relatorios = Relatorios(gerenciador_tarefas)

# Adicione mais rotas conforme necessário
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
