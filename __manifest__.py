{
    'name': "Employee Badge",
    'version': '1.0',
    'summary': 'Generate employee ID cards',
    'description': """
        This module allows you to generate and print ID cards/badges for employees.
        Features:
        - QR code generation for employee identification
        - Badge number management
        - PDF badge printing functionality
    """,
    'category': 'Human Resources',
    'author' : 'Gharel',
    'depends': ['hr'],
    'data': [
        'views/employee_badge_views.xml',
        'reports/employee_badge_report.xml',
        'reports/employee_badge_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}