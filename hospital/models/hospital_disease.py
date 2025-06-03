from odoo import fields, models


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'

    name = fields.Char(string="Disease Name",required=True)
    description = fields.Char(string="Description")
    contagiousness = fields.Selection(string="Contagiousness",selection=[('undetermined', 'Undetermined'), ('yes', 'Yes'), ('no', 'No')],default='undetermined')
    symptom_disease_ids = fields.One2many(
        'hospital.symptom.disease',
        'disease_id',
        string='Symptoms'
    )
    treatment_ids = fields.One2many(
        'hospital.treatment',
        'disease_id',
        string='Treatments'
    )
