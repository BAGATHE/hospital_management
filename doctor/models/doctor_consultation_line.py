from odoo import fields, models,api,_

class DoctorConsultationLine(models.Model):
    _inherit = 'hospital.consultation.line'

    total_price = fields.Float(compute='_compute_total_price', string="total price",store=True)
    equivalent_ids = fields.Many2many(
        'hospital.medicine',
        compute='_compute_equivalents',
        string='Equivalent Medicines',
        store=False,
    )

    @api.depends('medicine_id', 'quantity', 'medicine_price')
    def _compute_total_price(self):
        for line in self:
            line.total_price = line.quantity * line.medicine_price

    @api.onchange('quantity')
    def _onchange_quantity(self):
        if self.medicine_id:
            if self.quantity <= 0:
                self.quantity =1

    @api.onchange('duration')
    def _onchange_duration(self):
        if self.medicine_id:
            if self.duration <= 0:
                self.duration = 1

    @api.depends('medicine_id')
    def _compute_equivalents(self):
        for line in self:
            line.equivalent_ids = line.medicine_id.equivalent_ids

    @api.onchange('medicine_id')
    def _onchange_medicine(self):
        if self.medicine_id and self.medicine_id.equivalent_ids:
            return {
                'warning': {
                    'title': _("Equivalent Medicines Found"),
                    'message': _(
                        "There are equivalents: %s" % ", ".join(self.medicine_id.equivalent_ids.mapped('name')))
                }
            }



