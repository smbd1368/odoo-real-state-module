# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_recurring_plan(models.Model):
    _name = 'real_estate.crm_recurring_plan'
    _description = 'real_estate.crm_recurring_plan'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
