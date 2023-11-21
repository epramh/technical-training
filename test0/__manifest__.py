{
    'name': 'Test0', # The name that will appear in the App list
    'version': '1.0.0', # Version
    'summary': 'Test Customization',
    'sequence': 1,
    'description': """
    Long Description of your modules""",
    'author': 'Odooistic',
    'company': 'Company Name',
    'website': 'https://www.website.com',
    'category': 'Customization',
    'depends': ['base'], # dependencies
    'data': [
        # 'security/ir.model.access.csv',


    ],
    'application': True, # This line says the module is an App, and not a module
}
