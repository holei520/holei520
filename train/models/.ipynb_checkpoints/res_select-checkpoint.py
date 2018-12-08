from odoo import api, fields, models

class select(models.Model):
    _inherit = 'res.select'

    is_teacher = fields.Boolean(string='老师')
    is_student = fields.Boolean(string='学生')