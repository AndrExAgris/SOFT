class Grupo:
    def __init__(self, id_grupo, nome, descricao):
        self.id_grupo = id_grupo
        self.nome = nome
        self.descricao = descricao
        self.membros = []  # Lista para armazenar membros do grupo

    def adicionar_membro(self, usuario):
        self.membros.append(usuario)

    def remover_membro(self, usuario):
        self.membros.remove(usuario)

    def to_dict(self):
        return {
            'id_grupo': self.id_grupo,
            'nome': self.nome,
            'descricao': self.descricao,
            'membros': [membro.to_dict() for membro in self.membros]
        }
