# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta


class EstateProperties(models.Model):
    _name = 'property_offer_ids'
    _description = 'real_estate.property_offer_ids'
    _order = 'price desc'

    name = fields.Char(string="Name")
    price = fields.Float(string='Price')
    validity = fields.Integer(string='Validity', default=7)
    create_date = fields.Date(string='Date', default=fields.Date.context_today)
    date_deadline = fields.Date(string='Date Deadline', compute='_compute_date_deadline', store=True)
    status = fields.Selection([
        ('new', 'New'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', Readonly=True)

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for rec in self:
            if rec.create_date:
                rec.date_deadline = rec.create_date + timedelta(days=rec.validity)

    def action_accept(self):
        for record in self:
            if record.status != 'new':
                raise UserError("Only new properties can be accepted.")
            record.status = 'accepted'

    def action_refuse(self):
        for record in self:
            if record.status != 'new':
                raise UserError("Only new properties can be refused.")
            record.status = 'refused'
    # property_id = fields.Many2one('real_estate.estate.properties', string='Property', required=True)
