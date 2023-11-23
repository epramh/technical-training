# -*- coding: utf-8 -*-
from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string='Name', required=True)