from odoo import fields, models

class EstateProperty(models.Model):
    	_name = "estate_property"
    	_description = 'Real Estate Property'

	name = fieds.Char(required=True)
	description = fieds.Text()
	postcode = fields.Char()
	date_availability = fields.Date()
	expected_price = fields.Float()
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	livin_area = fields.Integer()
	facades = fields.Boolean()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection(
		string = 'Type',
		selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
		help = "Orientation is used to info the orientation of the garden")