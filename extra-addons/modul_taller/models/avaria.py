# -*- coding: utf-8 -*-

from odoo import fields, models


class TallerAvaria(models.Model):
    _name = 'taller.avaria'
    _description = 'Avaria'

    nom = fields.Char(string='Nom', required=True)
    descripcio = fields.Text(string='Descripcio')
    dataEntrada = fields.Date(string='Data Entrada')
    dataSortida = fields.Date(string='Data Sortida')
    preu = fields.Float(string='Preu')
    cotxe_id = fields.Many2one('taller.cotxe', string='Cotxe', required=True, ondelete='cascade')
