from odoo import fields, models,api
from datetime import date
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherits = {'res.users': 'user_id'}

    sex = fields.Selection(string="Sex", selection=[('male', 'Male'), ('female', 'Female')],required=True)
    blood_type = fields.Selection(string="Blood Type", selection=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],required=True)
    date_of_birth = fields.Date(string="Date of Birth",required=True)
    weight = fields.Float(string="Weight",required=True)
    user_id = fields.Many2one('res.users', string='User Account', required=True, ondelete='cascade')

    _sql_constraints = [
        ('unique_user_account','UNIQUE(user_id)','Each patient must have a unique user account.'),
        ('check_weight','CHECK(weight > 0)','weight cannot be negative')
    ]

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for patient in self:
            if patient.date_of_birth and patient.date_of_birth > date.today():
                raise ValidationError('date of birth should not be in the future')
