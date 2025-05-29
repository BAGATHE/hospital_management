# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Angelo",
    'website': "https://github.com/BAGATHE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Healthcare',
    'version': '0.1',
     'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hospital_doctor_views.xml',
        'views/hospital_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/doctor_demo.xml',
        'demo/nurse_demo.xml',
        'demo/patient_demo.xml',
        'demo/disease_demo.xml',
        'demo/symptom_demo.xml',
        'demo/symptom_disease_data.xml',
    ],
    'application': True,
    'installable': True,
}

