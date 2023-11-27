from flask import render_template, request, redirect, url_for, flash
from app import app, gerenciador_tarefas, relatorios
from notificacoes import enviar_notificacao
from formularios import CriarTarefaForm

# Rotas
@app.route('/')
def index():
    form = CriarTarefaForm()
    form.id_projeto.choices = [(projeto.id_projeto, projeto.nome) for projeto in gerenciador_tarefas.projetos]
    return render_template('index.html', projetos=gerenciador_tarefas.projetos, form=form)

@app.route('/criar_tarefa', methods=['POST'])
def criar_tarefa():
    form = CriarTarefaForm(request.form)

    if form.validate_on_submit():
        # Recupera os dados do formulário
        id_tarefa = form.id_tarefa.data
        titulo = form.titulo.data
        descricao = form.descricao.data
        responsavel_id = form.responsavel_id.data
        id_projeto = form.id_projeto.data

        # Cria a tarefa
        try:
            tarefa = gerenciador_tarefas.criar_tarefa(id_tarefa, titulo, descricao, responsavel_id, id_projeto)

            # Envia notificação ao responsável
            enviar_notificacao(responsavel_id, f'Nova tarefa atribuída: {tarefa.titulo}')

            flash('Tarefa criada com sucesso!', 'success')
        except ValueError as e:
            flash(str(e), 'error')

    return redirect(url_for('index'))
