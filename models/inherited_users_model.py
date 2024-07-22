from odoo import fields, models


class InheritedUsersModel(models.Model):
    _inherit = "res.users"
    # _name = 'real_estate.inherited_users_model'

    property_ids = fields.One2many('real_estate.estate_properties', 'seller', string="Property Ids ")
