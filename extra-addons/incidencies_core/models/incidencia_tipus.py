from odoo import fields, models


class IncidenciaTipus(models.Model):
    _name = 'incidencia.tipus'
    _description = 'Tipus d\'incidencia'

    name = fields.Char(string='Nom', required=True)
