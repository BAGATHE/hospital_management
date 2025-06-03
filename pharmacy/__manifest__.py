# -*- coding: utf-8 -*-
{
    'name': "pharmacy",

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
    'depends': ['base','product'],
    'icon': '/pharmacy/static/src/img/pharmacy.svg',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pharmacy_views.xml',
        'views/pharmacy_menus.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/pharmacy_data.xml',
    ],

    'application': True,
    'installable': True,
}

