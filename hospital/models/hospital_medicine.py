from odoo import models, fields, api


class HospitalMedicine(models.Model):
    _name = 'hospital.medicine'
    _inherits = {'product.product': 'product_id'}
    _description = 'Hospital Medicine'

    product_id = fields.Many2one(
        'product.product',
        required=True,
        ondelete='cascade',
        string='Linked Product'
    )

    dosage = fields.Char(string="Dosage")
    equivalent_ids = fields.Many2many(
        'hospital.medicine',
        'medicine_equivalent_rel',
        'medicine_id',
        'equivalent_id',
        string="Equivalent Medicines"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product_vals = {
                'name': vals.get('name'),
                'type': 'consu',
                'list_price': vals.get('list_price', 0.0),
            }
            product = self.env['product.product'].create(product_vals)
            vals['product_id'] = product.id
            vals.pop('name', None)
            vals.pop('list_price', None)
        return super().create(vals_list)

