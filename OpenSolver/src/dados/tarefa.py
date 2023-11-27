class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, responsavel, status="A fazer"):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def to_dict(self):
        return {
            'id_tarefa': self.id_tarefa,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'responsavel': self.responsavel.to_dict(), 
            'status': self.status
        }
