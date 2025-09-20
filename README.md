# Student Management — Submission Package

Thank you for reviewing my submission. This repository contains a simple Odoo module `student_management` built for the NN Services & Engineering Fresher assignment.

## What is included
- `student_management/` — Odoo module with models, views, security, and menu actions.
- `RECRUITER_README.md` — this file (instructions and test plan).
- `.gitignore`, `LICENSE`.

## Quick demo (what to expect)
1. After installing the module, a top-level menu **Student Management** appears.
2. Under it: **Students**, **Courses**, and **Students by Course**.
3. Create Courses first. Then create Students and enroll them via the Courses field (many2many).
4. Use **Students by Course** wizard to pick a course and view enrolled students.
5. In the Student form, click **Show Enrolled Courses** to open the course list filtered for that student.

## Installation (for reviewers)
Prerequisites:
- Odoo 16 running (Community Edition recommended)
- PostgreSQL

Steps:
1. Copy the `student_management` folder into your Odoo addons path (for example `C:/odoo/odoo-server/addons/`).
2. Restart Odoo server (or service).
3. Activate Developer Mode in Odoo.
4. Update Apps list: Apps → Update Apps List.
5. Search for **Student Management** and click Install.
6. Open `Student Management → Courses` to create courses, then `Student Management → Students` to create students and enroll them.

## Test cases for examiners
1. Create two courses: `CSE101` and `MAT101`.
2. Create student `Alice` and enroll both courses in the form's **Courses** field.
3. Create student `Bob` and enroll only `CSE101`.
4. Use `Students by Course` → pick `CSE101` → Show Students (Alice & Bob should appear).
5. Open `Alice` record → Click `Show Enrolled Courses` → should show `CSE101` and `MAT101`.

## Code notes (short)
- Many2many relation uses `relation='student_course_rel'` in both models to ensure single join table.
- Wizard is a `TransientModel` returning an action with domain to filter students.

## Troubleshooting
- If the module doesn't appear: ensure Developer Mode is on and Apps list is updated.
- If access errors appear: check `ir.model.access.csv` names are correct.

## Contact / Demo

Thank you — I am available for a live demo and to explain code in detail during interview.

Regards,
Janin A Apurba
