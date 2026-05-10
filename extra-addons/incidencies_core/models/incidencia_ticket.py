from odoo import fields, models


class IncidenciaTicket(models.Model):
    _name = 'incidencia.ticket'
    _description = 'Ticket d\'incidencia'
    _order = 'id desc'

    asunto = fields.Char(string='Asunto', required=True)
    aula_id = fields.Many2one('incidencia.ubicacio', string='Ubicacio')
    mensaje = fields.Text(string='Missatge', required=True)
    comentarios_tecnicos = fields.Text(string='Comentaris tecnics')
    tipus_id = fields.Many2one('incidencia.tipus', string='Tipus')
    state = fields.Selection(
        [
            ('rebuda', 'Rebuda'),
            ('en_proces', 'En proces'),
            ('resolta', 'Resolta'),
            ('tancada', 'Tancada'),
        ],
        string='Estat',
        default='rebuda',
        required=True,
    )
    user_id = fields.Many2one(
        'res.users',
        string='Solicitant',
        default=lambda self: self.env.user,
        required=True,
    )
    foto = fields.Binary(string='Foto')
    foto_filename = fields.Char(string='Nom foto')
