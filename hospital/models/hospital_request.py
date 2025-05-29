from odoo import fields, models

class HospitalRequest(models.Model):
    _name = 'hospital.request'
    _description = 'Hospital Request'

    request_date = fields.Date(string="Request Date",required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient",required=True)
    nurse_id = fields.Many2one('hospital.nurse', string="Nurse")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")