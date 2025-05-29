from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Hospital Patient'

    partner_id = fields.Many2one('res.partner', string="Related Partner", required=True, ondelete='cascade')

    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Sex", required=True)
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Blood Type", required=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    weight = fields.Float(string="Weight (kg)", required=True)
    user_id = fields.Many2one('res.users', string='Portal Account')

    _sql_constraints = [
        ('check_weight', 'CHECK(weight > 0)', 'Weight must be positive.'),
        ('unique_user_id', 'UNIQUE(user_id)', 'A user can only be linked to one patient.')
    ]

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > date.today():
                raise ValidationError("Date of birth cannot be in the future.")
