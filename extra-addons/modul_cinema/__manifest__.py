{
    'name': 'Mòdul Cinema',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Javi',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/pelicula_views.xml',
        'views/director_views.xml',
        'views/actor_views.xml',
        'views/genere_views.xml',
    ],
    'installable': True,
    'application': True,
}