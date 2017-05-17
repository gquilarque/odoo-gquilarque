# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque, <gabrielaquilarque97@gmail.com>
############################################################################
{
    'name': 'Partner Credit Limit',
    'version': '10.0.0.1.0',
    "license": "LGPL-3",
    "author": "Quilarque",
    'category': '',
    'sequence': 15,
    'summary': 'Credit Limit and Overdue Payments',
    'website': '',
    'depends': ['sale'],
    'data': [
        'views/sale_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
