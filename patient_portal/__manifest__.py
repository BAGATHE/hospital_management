# -*- coding: utf-8 -*-
{
    'name': "patient_portal",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

     'author': "Angelo",
    'website': "https://github.com/BAGATHE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',
    'license': 'LGPL-3',
    'category': 'Healthcare',

    # any module necessary for this one to work correctly
    'depends': ['hospital','portal'],
    'icon': '/patient_portal/static/src/img/patient.svg',
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'application': True,
    'installable': True,
}

