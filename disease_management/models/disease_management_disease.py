from odoo import fields, models


class HospitalDisease(models.Model):
    _name = 'disease_management.disease'
    _description = 'Disease'

    name = fields.Char(string="Disease Name",required=True)
    description = fields.Char(string="Description")
    contagiousness = fields.Selection(string="Contagiousness",selection=[('undetermined', 'Undetermined'), ('yes', 'Yes'), ('no', 'No')],required=True,default='undetermined')
    symptom_disease_ids = fields.One2many(
        'disease_management.symptom.disease',
        'disease_id',
        string='Symptoms'
    )
