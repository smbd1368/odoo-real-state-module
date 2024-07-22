# -*- coding: utf-8 -*-
{
    'name': 'real_estate',
    'version': '1.0',
    'summary': 'A brief description of my module.',
    'author': 'MDI',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menus.xml',
        'views/tag_menus.xml',
        'views/offer_menus.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': -100,
}
