from odoo import fields, models,api

class DoctorConsultationLine(models.Model):
    _inherit = 'hospital.consultation.line'

    total_price = fields.Float(compute='_compute_total_price', string="total price",store=True)

    @api.depends('medicine_id', 'quantity')
    def _compute_total_price(self):
        total = 0
        for line in self:
            total = total +   line.quantity * line.medicine_price

        self.total_price = total

    @api.onchange('quantity')
    def _onchange_quantity(self):
        if self.medicine_id:
            if self.quantity < 0:
                self.quantity =0

