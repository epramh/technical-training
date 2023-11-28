# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyTag(models.Model):
    _name ="estate.property.tag"
    _description = "Tag of Estate Property"
    _order="name"

    name = fields.Char(required=True)