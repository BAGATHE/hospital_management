from odoo import api, fields, models

class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _inherits = {'res.users': 'user_id'}
    _description = 'Hospital Nurse'

    license_number = fields.Char(string="License Number", required=True)
    start_service = fields.Date(string="Start Service", required=True)
    user_id = fields.Many2one('res.users', string='User Account', required=True, ondelete='cascade')

    _sql_constraints = [
        (
            'unique_license_number',
            'UNIQUE(license_number)',
            'The license number must be unique for each nurse.'
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        nurse_group = self.env.ref('hospital.group_hospital_nurse')
        for vals in vals_list:
            user_vals = {
                'name': vals.get('name'),
                'login': vals.get('login'),
                'password': vals.get('password'),
                'groups_id': [(6, 0, [nurse_group.id])]
            }
            user = self.env['res.users'].create(user_vals)
            vals['user_id'] = user.id
        return super().create(vals_list)


    def unlink(self):
        users = self.mapped('user_id')
        res = super().unlink()
        users.unlink()
        return res