# -*- coding: utf-8 -*-
{
    'name': 'Incidencies Users',
    'summary': 'Interficie simplificada per clients d\'incidencies',
    'description': 'Vista simplificada i regles de seguretat per usuaris clients.',
    'author': 'Institut',
    'website': 'https://example.com',
    'category': 'Services/Helpdesk',
    'version': '17.0.1',
    'depends': ['base', 'incidencies_core'],
    'data': [
        'security/incidencies_users_security.xml',
        'security/ir.model.access.csv',
        'views/incidencia_ticket_user_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
}
