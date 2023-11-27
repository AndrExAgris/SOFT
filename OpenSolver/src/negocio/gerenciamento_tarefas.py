from usuario import Usuario
from tarefa import Tarefa
from projeto import Projeto

class GerenciadorTarefas:
    def __init__(self):
        self.usuarios = []
        self.projetos = []

    def cadastrar_usuario(self, id_usuario, nome, email, senha):
        novo_usuario = Usuario(id_usuario, nome, email, senha)
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def criar_projeto(self, id_projeto, nome, descricao):
        novo_projeto = Projeto(id_projeto, nome, descricao)
        self.projetos.append(novo_projeto)
        return novo_projeto

    def criar_tarefa(self, id_tarefa, titulo, descricao, responsavel, id_projeto):
        projeto = next((projeto for projeto in self.projetos if projeto.id_projeto == id_projeto), None)
        if projeto:
            nova_tarefa = Tarefa(id_tarefa, titulo, descricao, responsavel)
            projeto.adicionar_tarefa(nova_tarefa)
            return nova_tarefa
        else:
            raise ValueError("Projeto não encontrado.")

    def atribuir_tarefa(self, id_tarefa, responsavel_id):
        tarefa = next((tarefa for projeto in self.projetos for tarefa in projeto.tarefas if tarefa.id_tarefa == id_tarefa), None)
        responsavel = next((usuario for usuario in self.usuarios if usuario.id_usuario == responsavel_id), None)
        
        if tarefa and responsavel:
            tarefa.responsavel = responsavel
            return tarefa
        else:
            raise ValueError("Tarefa ou responsável não encontrado.")

    def obter_tarefas_do_projeto(self, id_projeto):
        projeto = next((projeto for projeto in self.projetos if projeto.id_projeto == id_projeto), None)
        if projeto:
            return projeto.tarefas
        else:
            raise ValueError("Projeto não encontrado.")

    def to_dict(self):
        return {
            'usuarios': [usuario.to_dict() for usuario in self.usuarios],
            'projetos': [projeto.to_dict() for projeto in self.projetos]
        }
