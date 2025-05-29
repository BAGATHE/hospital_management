from odoo import fields, models

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherits = {'res.users': 'user_id'}
    _description = 'Hospital Doctor'

    license_number = fields.Char(string="License Number",required=True)
    start_service = fields.Date(string="Start Service",required=True)
    user_id = fields.Many2one('res.users', string='User Account', required=True, ondelete='cascade')
    _sql_constraints = [
        (
            'unique_license_number',
            'UNIQUE(license_number)',
            'The license number must be unique for each doctor.'
        ),
    ]