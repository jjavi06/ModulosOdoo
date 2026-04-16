from odoo import models, fields

class MusicaArtista(models.Model):
    _name = 'musica.artista'
    _description = 'Artista Musical'

    nom = fields.Char(string='Nom', required=True)
    datanaix = fields.Date(string='Data de Naixement')