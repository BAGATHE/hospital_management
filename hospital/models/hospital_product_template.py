from odoo import fields, models

class HospitalProductTemplate(models.Model):
    _inherit = 'product.template'

    is_medicine = fields.Boolean(string="Is a Medicine", default=False)