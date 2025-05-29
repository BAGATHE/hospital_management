from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class PatientPortalRequest(models.Model):
    _inherit = 'hospital.request'



    @api.constrains('request_date')
    def _check_request_date(self):
        for rec in self:
            if rec.request_date and rec.request_date < date.today():
                raise ValidationError("The request date cannot be earlier than today.")

    @api.constrains('symptom_request_ids')
    def _check_symptoms(self):
        for rec in self:
            if not rec.symptom_request_ids:
                raise ValidationError("Please select at least one symptom")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('doctor_id'):
                raise ValidationError("A doctor is required for a request via the portal.")
        return super().create(vals_list)
