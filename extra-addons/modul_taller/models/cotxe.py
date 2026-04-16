# -*- coding: utf-8 -*-

from odoo import fields, models


class TallerCotxe(models.Model):
    _name = 'taller.cotxe'
    _description = 'Cotxe'

    foto = fields.Binary(string='Foto')
    model = fields.Char(string='Model', required=True)
    matricula = fields.Char(string='Matricula', required=True)
    color = fields.Char(string='Color')
    dataCompra = fields.Date(string='Data Compra')
    avaria_ids = fields.One2many('taller.avaria', 'cotxe_id', string='Avaries')
