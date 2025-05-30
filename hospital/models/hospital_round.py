from odoo import fields, models,api


class HospitalRound(models.Model):
    _name = 'hospital.round'
    _description = 'Hospital Round'

    description = fields.Text(string='Description')
    round_date = fields.Date(string='Round Date',required=True)
    state = fields.Selection(string="State round",selection=[('planned', 'In comming'),('in_progress', 'In progress'),('done', 'Done')  ],default='planned')
    is_free = fields.Boolean(string='Patient Released',default=False)
    diagnosis = fields.Text(string='Diagnosis')
    hospitalized_patient_id = fields.Many2one('hospital.hospitalized.patient',required=True, ondelete='cascade')
    nurse_id = fields.Many2one('hospital.nurse',required=True, ondelete='cascade')



