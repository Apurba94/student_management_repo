from odoo import models, fields

class Student(models.Model):
    _name = "student.management.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    roll_no = fields.Char(string="Roll No")
    department = fields.Char(string="Department")
    course_ids = fields.Many2many(
        comodel_name="student.management.course",
        relation="student_course_rel",
        column1="student_id",
        column2="course_id",
        string="Courses"
    )

    def action_show_enrolled_courses(self):
        course_ids = self.course_ids.ids
        action = self.env.ref('student_management.action_course_tree').read()[0]
        if course_ids:
            action['domain'] = [('id', 'in', course_ids)]
        else:
            action['domain'] = [('id', '=', False)]
        return action
