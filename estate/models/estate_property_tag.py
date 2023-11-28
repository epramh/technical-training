from odoo import api, fields, models

class EstatePropertyTag(models.Model):
    _name ="estate.property.tag"
    _description = "Tag of estate property"
    _order="name"

    name = fields.Char(required=True)