# controllers/main.py
from odoo import http
from odoo.http import request

class ContratarForm(http.Controller):
    
    # Controlador para renderizar a página
    @http.route(['/contratar-plano'], type='http', auth="public", website=True)
    def contratar_plano(self):
        return request.render('devfazer-hire.contratar_plano_page')

    # Controlador para processar o formulário
    @http.route(['/contratar'], type='http', auth="public", website=True, methods=['POST'])
    def contratar_form(self, **post):
        # Pegando os dados do formulário
        nome = post.get('nome')
        email = post.get('email')
        telefone = post.get('telefone')
        empresa = post.get('empresa')
        plano = post.get('plano')
        
        # Printando os dados no log do Odoo (terminal)
        print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}, Empresa: {empresa}, Plano: {plano}")

        # Retornando um template de agradecimento
        return request.render('devfazer-hire.contratar_obrigado')
