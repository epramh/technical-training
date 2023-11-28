# -*- coding: utf-8 -*-
from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
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
    property_type_id = fields.Char()
    
    #Description
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
    property_type_id = fields.Many2one("estate.property.type", string="Property Types")
    user_id = fields.Many2one('res.users', string="Salesman", index=True, default=lambda self:self.env.user)
    partner_id = fields.Many2one("res.partner", string='Buyer', index=True, copy=False)
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many('estate.property.offer', "property_id", string='Offers')