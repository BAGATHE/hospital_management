from odoo import fields, models

class HospitalSymptom(models.Model):
    _name = "disease_management.symptom"
    _description = "Symptom"

    name = fields.Char(string="Symptom Name",required=True)
