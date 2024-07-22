# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class estate_properties(models.Model):
    _name = 'real_estate.estate_properties'
    _description = 'real_estate.estate_properties'
    _order = 'id desc'

    name = fields.Char(string="Name")
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string="Description")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    selling_price = fields.Float(string="Selling Price", readonly=True)
    postcode = fields.Integer(string="Postcode")
    living_area = fields.Float(string="Living Area sqm")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Float(string="Garden Area sqm")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')

    total_area = fields.Float(string="Total Area sqm", compute="_compute_total")

    property_type_id = fields.Float(string="Partner Type Id")
    property_type_ids = fields.Many2one("estate.properties.type", string="Property Type Id")
    status = fields.Selection([
        ('new', 'New'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], string='Status', Readonly=True)
    expected_price = fields.Float(string="Expected Price")

    buyer = fields.Many2one("res.partner", string="Buyer")
    seller = fields.Many2one("res.users", string="Salesman")
    tag_ids = fields.Many2many("estate_property_tag", string="Tag Ids")
    best_price = fields.Float(string='Best Price', compute='_compute_best_price', store=True)
    offer_ids = fields.Many2one('property_offer_ids', string='Offers')

    @api.onchange('garden')
    def _onchange_garden(self):

        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0.0

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = float(record.living_area) + float(record.garden_area)

    def action_cancel(self):
        for rec in self:
            if (self.status != 'sold'):
                self.write({'status': 'cancelled'})
            else:
                raise ValidationError("Sold Properties cannot be cancelled")

    def action_sold(self):
        for rec in self:
            if (self.status != 'cancelled'):
                self.write({'status': 'sold'})
            else:
                raise ValidationError("Cancelled Properties cannot be Sold")
