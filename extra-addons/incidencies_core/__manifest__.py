# -*- coding: utf-8 -*-
{
    'name': 'Incidencies Core',
    'summary': 'Base de gestio d\'incidencies de l\'institut',
    'description': 'Models principals, seguretat TIC, vistes i informe PDF per incidencies.',
    'author': 'Institut',
    'website': 'https://example.com',
    'category': 'Services/Helpdesk',
    'version': '17.0.1',
    'depends': ['base', 'web'],
    'data': [
        'security/incidencies_security.xml',
        'security/ir.model.access.csv',
        'data/incidencia_tipus_data.xml',
        'views/incidencia_tipus_views.xml',
        'views/incidencia_ubicacio_views.xml',
        'views/incidencia_ticket_views.xml',
        'views/menu.xml',
        'reports/incidencia_ticket_report.xml',
    ],
    'installable': True,
    'application': True,
}
