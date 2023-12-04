from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name ="estate.property.type"
    _description = "type of estate property"

    name = fields.Char(required=True)
    
    property_ids = fields.One2many('estate.property', 'property_type_id')

    _sql_constraints = [
        ('name', 'UNIQUE (name)', 'A property property type name must be unique!'),
    ]