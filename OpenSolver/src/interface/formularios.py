from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class CriarTarefaForm(FlaskForm):
    id_tarefa = StringField('ID da Tarefa', validators=[DataRequired()])
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    responsavel_id = StringField('ID do Responsável', validators=[DataRequired()])
    id_projeto = SelectField('Projeto', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Criar Tarefa')
