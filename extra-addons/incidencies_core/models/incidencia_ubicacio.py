from odoo import fields, models


class IncidenciaUbicacio(models.Model):
    _name = 'incidencia.ubicacio'
    _description = 'Ubicacio de la incidencia'

    name = fields.Char(string='Nom', required=True)
