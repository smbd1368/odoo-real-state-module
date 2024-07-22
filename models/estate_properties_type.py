from odoo import models, fields, api


class estate_properties_type(models.Model):
    _name = 'estate.properties.type'
    _description = 'estate properties type'
    _order = 'name'

    name = fields.Char(required=True)
    type = fields.Many2one(comodel_name='real_estate.estate_properties', string='Type')
    buyer = fields.Many2one(comodel_name='real_estate.estate_properties', string='Buyer')
    seller = fields.Many2one(comodel_name='real_estate.estate_properties', string='Seller')
    tag_ids = fields.Many2many("estate_property_tag", string="Tag Ids")
    property_id = fields.One2many('real_estate.estate_properties', 'property_type_ids', string='property id')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
