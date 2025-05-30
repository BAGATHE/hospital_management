from odoo import fields, models,api

class HospitalConsultationLine(models.Model):
    _name = 'hospital.consultation.line'
    _description = 'Hospital Consultation Line'

    medicine_id = fields.Many2one('hospital.medicine',required=True,ondelete='cascade')
    quantity = fields.Integer(string="Quantity", required=True)
    dosage = fields.Text(string="dosage")
    duration = fields.Integer(string="Duration in days")
    consultation_id = fields.Many2one('hospital.consultation',required=True,ondelete='cascade')

