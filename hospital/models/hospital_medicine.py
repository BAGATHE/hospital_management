from odoo import fields, models,api

class HospitalMedecine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Hospital Medicine'

    name = fields.Char(string = "medicine name", required=True)
