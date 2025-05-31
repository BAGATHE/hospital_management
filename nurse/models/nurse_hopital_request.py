from odoo import fields, models,api
from odoo.exceptions import ValidationError

class NurseHospitalRequest(models.Model):
    _inherit = 'hospital.request'

    patient_sex = fields.Selection(related='patient_id.sex', readonly=True)
    patient_blood_type = fields.Selection(related='patient_id.blood_type', readonly=True)
    patient_weight = fields.Float(related='patient_id.weight', readonly=True)



    def action_validate_request(self):
        self.ensure_one()
        consultation = self.env['hospital.consultation']

        consultation.sudo().create({
            'consultation_date':self.request_date,
            'doctor_id':self.doctor_id.id,
            'patient_id':self.patient_id.id,
            'is_hospitalized':False,
            'is_release_with_prescription':False,
            'request_id':self.id,
        })
        self.state = 'validated'

    def action_cancel_request(self):
        self.ensure_one()
        if self.state == 'validated':
            raise ValidationError(_("The patient has already been validated."))
        self.state = 'canceled'




