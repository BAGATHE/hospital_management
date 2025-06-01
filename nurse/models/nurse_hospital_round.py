from odoo import fields, models,api
from odoo.exceptions import ValidationError,UserError


class NurseHospitalRound(models.Model):
    _inherit = 'hospital.round'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        related='hospitalized_patient_id.patient_id',
        readonly=True,
        store=False,
    )

    @api.constrains('round_date', 'hospitalized_patient_id')
    def _check_duplicate_round(self):
        for rec in self:
            duplicate = self.search([
                ('hospitalized_patient_id', '=', rec.hospitalized_patient_id.id),
                ('round_date', '=', rec.round_date),
                ('id', '!=', rec.id)
            ])
            if duplicate:
                raise ValidationError(_(
                    "A round is already scheduled for this patient on the date : %s."
                ) % rec.round_date)

    def action_done_next(self):
        for rec in self:
            if rec.is_free:
                rec.state = 'done'
                rec.hospitalized_patient_id.state = 'discharged'
            else:
                if not rec.next_round_date:
                    raise UserError("Please enter the date of the next round.")
                if rec.next_round_date < rec.round_date:
                    raise UserError("the date cannot be earlier than the previous one")

                self.env['hospital.round'].create({
                    'hospitalized_patient_id': rec.hospitalized_patient_id.id,
                    'nurse_id': rec.nurse_id.id,
                    'round_date': rec.next_round_date,
                    'description': rec.description_next_round,
                    'state': 'planned'
                })

                if rec.hospitalized_patient_id.state == 'admitted':
                    rec.hospitalized_patient_id.state = 'under_treatment'
                elif rec.hospitalized_patient_id.state == 'under_treatment':
                    rec.hospitalized_patient_id.state = 'in_remission'

                rec.state = 'done'
