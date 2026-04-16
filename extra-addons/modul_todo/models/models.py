# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modul_todo(models.Model):
#     _name = 'modul_todo.modul_todo'
#     _description = 'modul_todo.modul_todo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

