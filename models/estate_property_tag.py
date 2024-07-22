from odoo import models, fields, api


class estate_properties_tag(models.Model):
    _name = 'estate_property_tag'
    _description = 'estate properties type'
    _order = 'name'

    name = fields.Char(string="Name",
                       required=True)
    tag_ids = fields.Many2many("estate.properties.type", string="Tag Ids")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
