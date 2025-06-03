from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Hospital Patient'



    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Sex", required=True)
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Blood Type", required=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    weight = fields.Float(string="Weight (kg)", required=True)
    user_id = fields.Many2one('res.users', string='Portal Account')
    partner_id = fields.Many2one('res.partner', string="Related Partner", required=True, ondelete='cascade')
    login = fields.Char(string="Login")
    password = fields.Char(string="Password")

    _sql_constraints = [
        ('check_weight', 'CHECK(weight > 0)', 'Weight must be positive.'),
        ('unique_user_id', 'UNIQUE(user_id)', 'A user can only be linked to one patient.')
    ]

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > date.today():
                raise ValidationError("Date of birth cannot be in the future.")

    @api.model_create_multi
    def create(self, vals_list):
        group_patient = self.env.ref('hospital.group_hospital_patient')

        for vals in vals_list:
            if vals.get('login') and vals.get('password'):
                user_vals = {
                    'name': vals.get('name'),
                    'login': vals['login'],
                    'password': vals['password'],
                    'email': vals.get('email', False),
                    'groups_id': [(6, 0, [group_patient.id])],
                    'partner_id': vals.get('partner_id'),
                }
                user = self.env['res.users'].create(user_vals)
                vals['user_id'] = user.id
            elif vals.get('login') or vals.get('password'):
                raise ValidationError("Both login and password must be provided to create a user account.")

        return super().create(vals_list)

    def unlink(self):
        users_to_delete = self.mapped('user_id')
        res = super().unlink()
        users_to_delete.unlink()
        return res



