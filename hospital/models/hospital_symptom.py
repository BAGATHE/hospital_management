from odoo import fields, models

class HospitalSymptom(models.Model):
    _name = "hospital.symptom"
    _description = "Symptom"

    name = fields.Char(string="Symptom Name",required=True)
