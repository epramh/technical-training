# -*- coding: utf-8 -*-
from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offer of Estate Property"
    _order =  'price desc'

    price = fields.Float()
    status = fields.Selection(
        string='Status',
        copy=False,
        help="Offer status is used to show the offer's status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
    )
    partner_id = fields.Many2one("res.partner", string='Partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)