from odoo import models, fields


class Avio(models.Model):
    _name = 'gestfly.avio'
    _description = 'Avio'

    codi = fields.Integer(string='Codi', required=True)
    imatge = fields.Image(string='Imatge')
    marca = fields.Integer(string='Marca')
    model = fields.Char(string='Model', required=True)
    max_vel = fields.Float(string='Max Vel')

    vol_ids = fields.One2many('gestfly.vol', 'avio_id', string='Vols')
