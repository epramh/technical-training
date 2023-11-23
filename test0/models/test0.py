# -*- coding: utf-8 -*-
from odoo import fields, models

class Test0(models.Model):
    _name = "test0"
    _description = 'The Test 0'

    name = fields.Char(required=True)
    age = fields.Integer(string="Age")