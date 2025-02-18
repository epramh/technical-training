# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, exceptions, tools

from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from decimal import *

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = "id desc"

    name = fields.Char(
        string='Title',
        required=True
        ) #Inside '()' for specification
    # last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        'Available From',copy=False, 
        default=lambda self: fields.Datetime.today() + relativedelta(months=+3)
    )
    expected_price = fields.Float(
        required=True
    )
    selling_price = fields.Float(
        readonly=True, 
        copy=False
    )
    property_type_id = fields.Char()
    
    #Description
    bedrooms = fields.Integer(
        default="2"
        )
    living_area = fields.Integer(
        string='Living Area (sqm)'
    )
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(
        string='Garden Area (sqm)'
    )
    garden_orientation = fields.Selection(
        [('north', 'North'), 
        ('south', 'South'), 
        ('east', 'East'), 
        ('west', 'West')], 
        help = "Orientation is used to info the orientation of the garden"
    )
    
    active = fields.Boolean(#'Active',
        default=True,)
    state = fields.Selection(
        [('new', 'New'), ('offer received', 'Offer Received'),
        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'),
        ('canceled', 'Canceled')],
        required=True,
        copy=False,
        default='new'
    )
    status = fields.Selection(
        selection= [('new','New'),('canceled','Canceled'),('sold','Sold')],
        copy=False,
        default = 'new'
    )
    property_type_id = fields.Many2one(
        "estate.property.type", 
        string="Property Types"
    )
    user_id = fields.Many2one(
        'res.users', 
        string="Salesman", 
        index=True, 
        default=lambda self:self.env.user
    )
    partner_id = fields.Many2one(
        "res.partner", 
        string='Buyer', 
        index=True, 
        copy=False
    )
    tag_ids = fields.Many2many(
        'estate.property.tag', 
        string="Tags"
    )
    offer_ids = fields.One2many(
        'estate.property.offer', 
        "property_id"
    )

    total_area = fields.Integer(
        'Total Area (sqm)', 
        compute="_compute_total_area"
    )
    best_price = fields.Float(
        'Best Offer',
        compute="_compute_best_price"
    )
    message = fields.Text()

    # SQL constraints
    _sql_constraints = [
    #    ('check_expected_price', 'CHECK(expected_price > 0)', 'A property expected price must be strictly positive.'),
        ('check_selling_price', 'CHECK(selling_price => 0)', 'A property expected price must be strictly positive.')
    ]

    # Python constraints
    @api.constrains('expected_price')
    def _check_expected_price(self):
        for rec in self:
            if rec.expected_price < 0:
                raise ValidationError(_('A property expected price must be strictly positive.'))
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price")) if len(record.offer_ids)>0 else 0
    
    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if self.garden:
                self.garden_area = 10
                self.garden_orientation = 'north'
                self.message = 'This check the garden option : add 10 in the garden_area and North in the garden_orientation'
            # return {'warning': {
            #     'title': _("Warning"),
            #     'message': ('This check the garden option : add 10 in the garden_area and North in the garden_orientation')}}
            else:
                self.garden_area = None
                self.garden_orientation = ""
                self.message = 'This uncheck the garden option : remove 10 in the garden_area and North in the garden_orientation'
            # return {'warning': {
            #     'title': _("Warning"),
            #     'message': ('This uncheck the garden option : remove 10 in the garden_area and North in the garden_orientation')}}
    
    def action_sold(self):
        for record in self:
            if self.status=='new':
                self.status='sold'
                self.state='sold'
                return True
            elif record.status=='canceled':
                raise exceptions.UserError("Canceled property cannot be sold!")
            else:
                raise exceptions.UserError("The property has been sold")

    def action_cancel(self):
        for record in self:
            if self.status=='new':
                self.status='canceled'
                self.state='canceled'
                return True
            elif record.status=='sold':
                raise exceptions.UserError("Sold property cannot be canceled!")
            else:
                raise exceptions.UserError("The property has been canceled")
    
        # SQL constraints
    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price => (0.9*expected_price))', "The selling price cannot be lower than '90%' of the expected price.")
    ]
    # Python constraints
    # @api.constrains('selling_price', 'expected_price')
    # def _check_expected_pric(self):
    #     for record in self:

    #         if rec.expected_price < 0:
    #             raise ValidationError(_('The selling price cannot be lower than 90 percent of the expected price.'))
    