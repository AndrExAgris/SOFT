from flask_socketio import SocketIO

socketio = SocketIO()

def configurar_socketio(app):
    socketio.init_app(app)

def enviar_notificacao(usuario_id, mensagem):
    socketio.emit(f'notificacao_{usuario_id}', {'mensagem': mensagem}, namespace='/notificacoes')

