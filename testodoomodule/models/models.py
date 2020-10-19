# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/ud/odoo/custom/testodoomodule(models.Model):
#     _name = '/home/ud/odoo/custom/testodoomodule./home/ud/odoo/custom/testodoomodule'
#     _description = '/home/ud/odoo/custom/testodoomodule./home/ud/odoo/custom/testodoomodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
