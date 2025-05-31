from odoo import fields, models,api

class HospitalConsultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Hospital Consultation'

    consultation_date = fields.Date('Consultation Date',required=True)
    advice = fields.Html('Advice')
    state = fields.Selection(string="Consultation state", selection=[('draft','Draft'),('in_progress','In Progress'),('completed','Completed'),('canceled','Canceled')],default='draft')
    diagnosis = fields.Text(string='Patient Diagnosis')
    doctor_id = fields.Many2one('hospital.doctor',required=True,ondelete='cascade')
    request_id = fields.Many2one('hospital.request',required=True,ondelete='cascade')
    disease_id =  fields.Many2one('hospital.disease',ondelete='cascade',default=None)
    consultation_line_ids = fields.One2many('hospital.consultation.line','consultation_id',string='Consultation Lines')
    patient_id = fields.Many2one('hospital.patient', string='Patient', related='request_id.patient_id', store=True, readonly=True)
