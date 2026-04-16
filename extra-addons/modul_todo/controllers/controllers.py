# -*- coding: utf-8 -*-
# from odoo import http


# class ModulTodo(http.Controller):
#     @http.route('/modul_todo/modul_todo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modul_todo/modul_todo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modul_todo.listing', {
#             'root': '/modul_todo/modul_todo',
#             'objects': http.request.env['modul_todo.modul_todo'].search([]),
#         })

#     @http.route('/modul_todo/modul_todo/objects/<model("modul_todo.modul_todo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modul_todo.object', {
#             'object': obj
#         })

