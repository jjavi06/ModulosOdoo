from odoo import models, fields


class Vol(models.Model):
    _name = 'gestfly.vol'
    _description = 'Vol'

    codi = fields.Integer(string='Codi', required=True)
    passatgers = fields.Integer(string='Passatgers')
    data_sortida = fields.Date(string='Data Sortida')
    data_arrivada = fields.Date(string='Data Arrivada')

    origen_id = fields.Many2one(
        'gestfly.aeroport',
        string='Origen',
        ondelete='restrict',
        required=True
    )
    desti_id = fields.Many2one(
        'gestfly.aeroport',
        string='Desti',
        ondelete='restrict',
        required=True
    )
    avio_id = fields.Many2one(
        'gestfly.avio',
        string='Avio',
        ondelete='set null'
    )
