from odoo import fields, models,api

class HospitalConsultationLine(models.Model):
    _name = 'hospital.consultation.line'
    _description = 'Hospital Consultation Line'

    medicine_id = fields.Many2one('hospital.medicine',required=True,ondelete='cascade')
    quantity = fields.Integer(string="Quantity", required=True)
    dosage = fields.Text(string="dosage")
    duration = fields.Integer(string="Duration in days",required=True,default=1)
    consultation_id = fields.Many2one('hospital.consultation',required=True,ondelete='cascade')
    medicine_price =fields.Float(related='medicine_id.list_price',string="price")

    _sql_constraints = [
        ('positive_quantity', 'CHECK(quantity > 0)', 'The quantity must be greater than zero.'),
        ('positive_duration', 'CHECK(duration >= 0)', 'The duration must be a non-negative number.'),
        ('unique_medicine_per_consultation', 'UNIQUE(consultation_id, medicine_id)', 'Each medicine should appear only once per consultation.')
    ]




