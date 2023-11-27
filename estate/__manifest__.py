{
    'name': 'Real Estate', # The name that will appear in the App list
    'version': '1.0.0', # Version
    'summary': 'Odoo 16 Test Development',
    'sequence': 3,
    'description': """
    Long Description of your modules""",
    'author': 'Ravo',
    'company': 'MGBI',
    #'website': 'https://www.mgbi.tech',
    'category': 'Customization',
    'depends': ['base'], # dependencies
    'data': [
        'security/ir.model.access.csv',
        
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
    ],

    'installable': True,
    'application': True, # This line says the module is an App, and not a module
    'license': 'LGPL-3',
}