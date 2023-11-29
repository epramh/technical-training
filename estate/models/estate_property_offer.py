# -*- coding: utf-8 -*-
from odoo import api, fields, models
import datetime

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
    partner_id = fields.Many2one(
        "res.partner", 
        string='Partner', 
        required=True
    )
    property_id = fields.Many2one(
        'estate.property', 
        required=True
    )

    validity = fields.Integer(
        'Validity (days)',
        default=7
    )
    date_deadline = fields.Date(
        'Deadline',
        compute="_compute_date_deadline",
        inverse='_compute_date_deadline'
    )

    @api.depends("create_date", 'validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = (
                record.create_date if record.create_date else datetime.date.today()
            ) + datetime.timedelta (days = record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days