from odoo import fields, models

class DoctorHospitalPatient(models.Model):
    _inherit = 'hospital.patient'

    consultation_ids = fields.One2many('hospital.consultation','patient_id', string='Consultations completed')