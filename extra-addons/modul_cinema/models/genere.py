from odoo import models, fields

class Genere(models.Model):
    _name = 'cinema.genere'
    _description = 'Gènere Cinematogràfic'

    nom = fields.Char(string='Nom', required=True)
    foto = fields.Image(string='Foto')
    activo = fields.Boolean(string='Actiu', default=True)
    
    # Relacions
    pelicula_ids = fields.Many2many('cinema.pelicula', 'cinema_pelicula_genere_rel', 'genere_id', 'pelicula_id', string='Pel·lícules')
    
    # Camps calculats
    num_pelicules = fields.Integer(string='Nombre de pel·lícules', compute='_compute_num_pelicules', store=False)
    
    def _compute_num_pelicules(self):
        for record in self:
            record.num_pelicules = len(record.pelicula_ids)