
from odoo import api, fields, models

class TrainingLesson(models.Model):
    _name = 'pscloud.train.lesson'
    _description = "课程"

    name = fields.Char(string='课程名称',size=64,default='默认的名称')


    teacher_id = fields.Many2one('res.select', string='老师', domain=[('is_teacher', '=', True)])
    student_ids = fields.Many2many('res.select', string='学生', domain=[('is_student', '=', True)], readonly=True)
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')


    seat_qty = fields.Integer(string='座位数')
    
    desc = fields.Text(string='描述')

