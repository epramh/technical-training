# -*- coding: utf-8 -*-
from odoo import fields, models
from dateutil.relativedelta import relativedelta

class HospitalPatient(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(
        string='Title',
        required=True
        ) #Inside '()' for specification
    # last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        'Available From',copy=False, 
        default=lambda self: fields.Datetime.today() + relativedelta(months=+3)) # Or fields.Datetime.today()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(
        readonly=True, 
        copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [('north', 'North'), 
        ('south', 'South'), 
        ('east', 'East'), 
        ('west', 'West')], 
        help = "Orientation is used to info the orientation of the garden")
    active = fields.Boolean(#'Active',
        default=True,)
    state = fields.Selection(
        [('new', 'New'),
        ('offer received', 'Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')],
        required=True,
        copy=False,
        default='new'
    )