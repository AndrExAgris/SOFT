from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO
from gerenciador_tarefas import GerenciadorTarefas
from notificacoes import socketio, configurar_socketio
from relatorios import Relatorios

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretpassword'  
configurar_socketio(app)

gerenciador_tarefas = GerenciadorTarefas()
relatorios = Relatorios(gerenciador_tarefas)

# Rotas
@app.route('/')
def index():
    return render_template('index.html', projetos=gerenciador_tarefas.projetos)

# Adicione mais rotas conforme necessário

if __name__ == '__main__':
    socketio.run(app, debug=True)
