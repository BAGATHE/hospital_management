from odoo import fields, models


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Hospital Disease'

    name = fields.Char(string="Disease Name",required=True)
    description = fields.Char(string="Description")
    contagiousness = fields.Selection(string="Contagiousness",selection=[('undetermined', 'Undetermined'), ('yes', 'Yes'), ('no', 'No')],required=True,default='undetermined')
