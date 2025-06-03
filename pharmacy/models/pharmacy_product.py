from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta, date

class PharmacyProduct(models.Model):
    _name = 'pharmacy.product'
    _description = 'Pharmacy-specific product info'

    pharmacy_id = fields.Many2one('pharmacy.pharmacy', required=True)
    product_id = fields.Many2one('product.product', required=True)
    category = fields.Char(related='product_id.product_tmpl_id.categ_id.name',string='category',store=True)
    price = fields.Float(string="Selling price")
    restock_delay = fields.Integer(string="Replenishment time (days)")
    equivalent_ids = fields.Many2many('product.product', string="Equivalent drugs")
    next_available_date = fields.Date(compute='_compute_next_available')

    stock = fields.Float(string="stock qtt")


    def _compute_next_available(self):
        for rec in self:
            if rec.stock == 0:
                rec.next_available_date = date.today() + timedelta(days=rec.restock_delay)
            else:
                rec.next_available_date = False