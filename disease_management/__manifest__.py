# -*- coding: utf-8 -*-
{
    'name': "disease_management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Lolo",
    'website': "https://github.com/BAGATHE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full lists
    'version': '0.1',
    'license': 'LGPL-3',
    'category': 'Healthcare',

    # any module necessary for this one to work correctly
    'depends': ['base','hospital'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/disease_views.xml',
        'views/symptom_views.xml',
        'views/disease_management_menus_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'installable': True,
}

