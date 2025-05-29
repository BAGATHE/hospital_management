from odoo import api, fields, models
from odoo.api import ondelete


class HospitalSymptomRequest(models.Model):
    _name = 'hospital.symptom.request'
    _description = 'Hospital Symptom Request'

    symptom_id = fields.Many2one('hospital.symptom',required=True, ondelete='cascade')
    request_id = fields.Many2one('hospital.request',ondelete='cascade', required=True)