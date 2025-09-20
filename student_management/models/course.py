from odoo import models, fields

class Course(models.Model):
    _name = "student.management.course"
    _description = "Course"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    credit = fields.Float(string="Credit")
    student_ids = fields.Many2many(
        comodel_name="student.management.student",
        relation="student_course_rel",
        column1="course_id",
        column2="student_id",
        string="Students"
    )
