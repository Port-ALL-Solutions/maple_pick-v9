# -*- coding: utf-8 -*-
{
    'name': "Bons de cueillette",

    'summary': """
	Bon de cueillette des barils
				""",

    'description': """
	Création et suivi des cueillettes de sirop d'érable (initiée par les commandes de sirop).  Assignation et
	gestion des chauffeurs et transporteurs.
    """,

    'author': "Global Technologie",
    'website': "http://www.globaltechnologie.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['mapleorder'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
#        'views/templates.xml',
    ],
    # only loaded in demonstration mode
 #   'demo': [
 #       'demo/demo.xml',
#    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}