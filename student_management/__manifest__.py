{
    "name": "Student Management",
    "version": "16.0.1.0.0",
    "summary": "Simple student and course management (many2many) for fresher assignment",
    "author": "Janin A Apurbo",
    "category": "Education",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_views.xml",
        "views/course_views.xml",
        "views/wizard_views.xml",
        "data/menus_actions.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
