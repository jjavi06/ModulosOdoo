from odoo import models, fields


class Aeroport(models.Model):
    _name = 'gestfly.aeroport'
    _description = 'Aeroport'

    codi = fields.Integer(string='Codi', required=True)
    nom = fields.Char(string='Nom', required=True)
    imatge = fields.Image(string='Imatge')
    ciutat = fields.Char(string='Ciutat')
    pais = fields.Char(string='Pais')
    latitud = fields.Float(string='Latitud')
    longitud = fields.Float(string='Longitud')

    vol_origen_ids = fields.One2many(
        'gestfly.vol',
        'origen_id',
        string='Vols Origen'
    )
    vol_desti_ids = fields.One2many(
        'gestfly.vol',
        'desti_id',
        string='Vols Desti'
    )
