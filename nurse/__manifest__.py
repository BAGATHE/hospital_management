# -*- coding: utf-8 -*-
{
    'name': "nurse",

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
    'depends': ['hospital'],
    'icon': '/nurse/static/src/img/nurse.svg',
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hospital_request_views.xml',
        'views/hospitalized_patient_views.xml',
        'views/hospital_round_views.xml',
        'report/nurse_hospital_round_report.xml',
        'report/nurse_hospital_round_report_template.xml',
        'views/nurse_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable': True,
}

