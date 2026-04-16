from odoo import models, fields
from datetime import datetime

class Director(models.Model):
    _name = 'cinema.director'
    _description = 'Directori Cinematogràfic'

    nom = fields.Char(string='Nom', required=True)
    cognom = fields.Char(string='Cognom', required=True)
    data_naixement = fields.Date(string='Data de Naixement')
    bibliografia = fields.Text(string='Bibliografia')
    
    # Relacions
    pelicula_ids = fields.One2many('cinema.pelicula', 'director_id', string='Pel·lícules')
    
    # Camps calculats
    edat = fields.Integer(string='Edat', compute='_compute_edat', store=False)
    
    def _compute_edat(self):
        any_actual = datetime.now().year
        for record in self:
            if record.data_naixement:
                record.edat = any_actual - record.data_naixement.year
            else:
                record.edat = 0
    
    def name_get(self):
        res = []
        for record in self:
            name = f"{record.nom} {record.cognom}"
            res.append((record.id, name))
        return res