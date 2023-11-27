class Relatorios:
    def __init__(self, gerenciador_tarefas):
        self.gerenciador_tarefas = gerenciador_tarefas

    def gerar_relatorio_funcionarios(self):
        funcionarios = self.gerenciador_tarefas.usuarios
        relatorio = []

        for usuario in funcionarios:
            relatorio.append({
                'id_usuario': usuario.id_usuario,
                'nome': usuario.nome,
                'email': usuario.email,
            })

        return relatorio

    def gerar_relatorio_grupos(self):
        grupos = self.gerenciador_tarefas.grupos
        relatorio = []

        for grupo in grupos:
            relatorio.append({
                'id_grupo': grupo.id_grupo,
                'nome': grupo.nome,
                'descricao': grupo.descricao,
            })

        return relatorio

    def gerar_relatorio_projetos(self):
        projetos = self.gerenciador_tarefas.projetos
        relatorio = []

        for projeto in projetos:
            relatorio.append({
                'id_projeto': projeto.id_projeto,
                'nome': projeto.nome,
                'descricao': projeto.descricao,
            })

        return relatorio
