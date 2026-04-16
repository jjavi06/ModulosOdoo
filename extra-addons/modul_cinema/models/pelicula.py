from odoo import models, fields
from datetime import datetime

class Pelicula(models.Model):
    _name = 'cinema.pelicula'
    _description = 'Pel·lícula Cinematogràfica'

    titol = fields.Char(string='Títol', required=True)
    pais = fields.Char(string='País d\'origen')
    any = fields.Integer(string='Any de llançament')
    duracio = fields.Integer(string='Duració (minuts)')
    puntuacio = fields.Float(string='Puntuació', digits=(2, 1))
    resum = fields.Text(string='Resum')
    foto = fields.Image(string='Foto')
    activo = fields.Boolean(string='Actiu', default=True)
    
    # Relacions
    director_id = fields.Many2one('cinema.director', string='Director', ondelete='set null')
    actor_ids = fields.Many2many('cinema.actor', 'cinema_pelicula_actor_rel', 'pelicula_id', 'actor_id', string='Actors')
    genere_ids = fields.Many2many('cinema.genere', 'cinema_pelicula_genere_rel', 'pelicula_id', 'genere_id', string='Gèneres')
    
    # Camps calculats
    antiguitat = fields.Integer(string='Antiguitat (anys)', compute='_compute_antiguitat', store=False)
    
    def _compute_antiguitat(self):
        any_actual = datetime.now().year
        for record in self:
            if record.any:
                record.antiguitat = any_actual - record.any
            else:
                record.antiguitat = 0