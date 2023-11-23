{
    'name': 'Apps', # The name that will appear in the App list
    'version': '1.0.0', # Version
    'summary': 'Odoo 16 Test Development',
    'sequence': 1,
    'description': """
    Long Description of your modules""",
    'author': 'Ravo',
    'company': 'MGBI',
    #'website': 'https://www.odoomates.tech',
    'category': 'Customization',
    'depends': ['base'], # dependencies
    'data': [
        #'security/ir.model.access.csv',
        #'views/menu.xml',
        #'views/patient.xml',
        #'security/ir.model.access.csv'
    ],

    'installable': True,
    'application': True, # This line says the module is an App, and not a module
    'license': 'LGPL-3',
}