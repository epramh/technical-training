{
    'name': 'Custom Odoo Website Qweb Template', # The name that will appear in the App list
    'version': '1.0.0', # Version
    'summary': 'Odoo 16 Development',
    'sequence': 3,
    'description': """
    Long Description of your modules""",
    'author': 'Ravo',
    'company': 'MGBI',
    #'website': 'https://www.localhost.com',
    'category': 'Customization',
    'depends': [
        'base',
        'website'
    ], # dependencies
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/menu.xml',
        'views/custom_website.xml'
    ],

    'installable': True,
    'application': False, # This line says the module is an App, and not a module
    'license': 'LGPL-3',
}
