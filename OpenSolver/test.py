from app import app
import unittest

class TestaPagina(unittest.TestCase):

    def setUp(self):
        test_app = app.test_client()
        self.response = test_app.get("/home")

    #testa resposta da pagina
    def test_html_string_reponse(self):
        response = "Sistema de Gestão de Tarefas"
        self.assertIn(response,self.response.data.decode("utf-8"))


    
class TestaClienteCadastro(unittest.TestCase):

    def setUp(self):
        test_app = app.test_client()
        self.response = test_app.get("/cadastro")
    
    def test_html_string_reponse(self):
        response = "Nome de usuario"
        self.assertIn(response,self.response.data.decode("utf-8"))

    def test_html_string_reponse(self):
        response = "email"
        self.assertIn(response,self.response.data.decode("utf-8"))

    def test_html_string_reponse(self):
        response = "Senha"
        self.assertIn(response,self.response.data.decode("utf-8"))

class TestaClienteLogin(unittest.TestCase):

    def setUp(self):
        test_app = app.test_client()
        self.response = test_app.get("/login")
    
    def test_html_string_reponse(self):
        response = "usuarioEncontrado"
        self.assertIn(response,self.response.data.decode("utf-8"))

    def test_html_string_reponse(self):
        response = "Usuario não existe"
        self.assertIn(response,self.response.data.decode("utf-8"))

    def test_html_string_reponse(self):
        response = "listaUsuarios"
        self.assertIn(response,self.response.data.decode("utf-8"))