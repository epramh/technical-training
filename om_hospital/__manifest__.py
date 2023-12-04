{
    'name': 'Hospital Management System', # The name that will appear in the App list
    'version': '1.0.0', # Version
    'summary': 'Odoo 16 Development',
    'sequence': 3,
    'description': """
    Long Description of your modules""",
    'author': 'Odoo Mates',
    'company': 'Company Name',
    #'website': 'https://www.odoomates.tech',
    'category': 'Customization',
    'depends': [
        'base',
        'mail'
    ], # dependencies
    'data': [
        #'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'security/ir.model.access.csv'
    ],

    'installable': True,
    'application': True, # This line says the module is an App, and not a module
    'license': 'LGPL-3',
}
