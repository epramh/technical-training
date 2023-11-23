# -*- coding: utf-8 -*-
from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "apps"
    _description = "Apps for Testing Purpose"

    name = fields.Char(string='Name', required=True)