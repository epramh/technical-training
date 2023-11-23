# -*- coding: utf-8 -*-
from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string='Name', required=True) #Inside '()' for specification
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], help = "Orientation is used to info the orientation of the garden")