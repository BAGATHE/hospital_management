from odoo import models, fields, api


class PharmacyPharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = 'Pharmacie'

    name = fields.Char(string='pharmacie name', required=True)
    partner_id = fields.Many2one('res.partner', string='associated supplier', required=True)
    delay_out_of_stock = fields.Integer(string="Replenishment time (days)", default=7)
    pharmacy_product_ids = fields.One2many('pharmacy.product', 'pharmacy_id', string='Médicaments')

    @api.model_create_multi
    def create(self, vals):
        pharmacy = super(PharmacyPharmacy, self).create(vals)
        pharmacy.partner_id.supplier_rank = 1
        return pharmacy
