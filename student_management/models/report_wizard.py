from odoo import models, fields

class StudentCourseReportWizard(models.TransientModel):
    _name = "student.management.report.wizard"
    _description = "Wizard to show students for selected course"

    course_id = fields.Many2one('student.management.course', string="Course", required=True)

    def action_open_students(self):
        action = self.env.ref('student_management.action_student_tree').read()[0]
        if self.course_id:
            action['domain'] = [('course_ids', 'in', [self.course_id.id])]
        return action
