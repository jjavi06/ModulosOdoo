from odoo import fields, models

class TodoTasca(models.Model):
    _name = 'todo.tasca'
    _description = 'Tasca Todo'

    titol = fields.Char(string='Títol', required=True)
    data_inici = fields.Date(string='Data d\'inici')
    data_final = fields.Date(string='Data final')