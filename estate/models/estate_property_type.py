from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name ="estate.property.type"
    _description = 'House'

    name = fields.Char(required=True)