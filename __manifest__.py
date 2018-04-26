# -*- coding: utf-8 -*-
{
    'name': "todolist",

    'summary': """
       TODO list es un modulo para realizar lista de tareas en odoo""",

    'description': """
        Desarrollado para odoo 10 con python DAM2 por Aaron Salvador y David Ramírez
    """,

    'author': "clot",
    'website': "clot",

    'category': 'Uncategorized',
    'version': '0.2',

    'depends': ['base'],

    'data': [
        'views/mymenu.xml',
        'views/mainpage.xml',
    ],
    'application': True,   
}
