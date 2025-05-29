from odoo import models, fields, api

class HospitalSymptomDisease(models.Model):
    _name = 'hospital.symptom.disease'
    _description = 'symptom gravity hospital'

    disease_id = fields.Many2one('hospital.disease',required=True, ondelete='cascade')
    symptom_id = fields.Many2one('hospital.symptom',required=True, ondelete='cascade')
    gravity = fields.Integer(string='Gravity',default=1)

    _sql_constraints = [
        ('check_symptom_disease','UNIQUE(disease_id,symptom_id)','this combinaiton already exists!'),
        ('check_gravity','CHECK(gravity>0)','Gravity must be greater than 0'),
    ]