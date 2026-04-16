from odoo import models, fields

class MusicaCanco(models.Model):
    _name = 'musica.canco'
    _description = 'Cançó'

    titol = fields.Char(string='Títol', required=True)
    minuts = fields.Float(string='Minuts')
    letra = fields.Text(string='Lletra')
    artista_id = fields.Many2one('musica.artista', string='Artista')