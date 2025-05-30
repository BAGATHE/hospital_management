from odoo import fields, models

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Hospital Treatment'

    disease_id = fields.Many2one('hospital.disease',required=True,ondelete='cascade')
    medicine_id = fields.Many2one('hospital.medicine',required=True,ondelete='cascade')