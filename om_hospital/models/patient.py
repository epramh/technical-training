# -*- coding: utf-8 -*-
from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Records"

    name = fields.Char(string='Name', required=True)
    #description = fields.Text(string='Description')
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="Is Child ?")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    