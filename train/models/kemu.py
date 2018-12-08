
from odoo import api, fields, models

class TrainingSubject(models.Model):
    _name = 'pscloud.train.kemu'
    _description = "科目"

    name = fields.Char(string='名称',size=64,default='默认的名称')
    person_id = fields.Many2one('res.select', string='负责人')
    lesson_ids = fields.One2many('pscloud.train.lesson', 'subject_id', string='课程')
    desc = fields.Text(string='描述')