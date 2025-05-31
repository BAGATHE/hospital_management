from odoo import fields, models

class NurseHospitalizedPatient(models.Model):
    _inherit = 'hospital.hospitalized.patient'

    def action_schedule_round(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'New Round',
            'res_model': 'hospital.round',
            'view_mode': 'form',
            'target': 'new', 
            'context': {
                'default_hospitalized_patient_id': self.id
            }
        }
