class Projeto:
    def __init__(self, id_projeto, nome, descricao):
        self.id_projeto = id_projeto
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

    def notificar_membros(self, mensagem):
        socketio.emit(f'notificacao_projeto_{self.id_projeto}', {'mensagem': mensagem}, namespace='/notificacoes')
        pass

    def progresso_do_projeto(self):
        if not self.tarefas:
            return 0.0  

        tarefas_concluidas = sum(1 for tarefa in self.tarefas if tarefa.status == 'Concluída')
        progresso = (tarefas_concluidas / len(self.tarefas)) * 100.0
        return round(progresso, 2) 
        pass

    def to_dict(self):
        return {
            'id_projeto': self.id_projeto,
            'nome': self.nome,
            'descricao': self.descricao,
            'tarefas': [tarefa.to_dict() for tarefa in self.tarefas]
        }
