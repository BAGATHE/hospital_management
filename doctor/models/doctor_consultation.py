from odoo import fields, models,api,_
from odoo.exceptions import UserError,ValidationError

from datetime import date

class DoctorConsultation(models.Model):
    _inherit = 'hospital.consultation'

    treatment_duration_days = fields.Integer('Treatment Duration Days',store=True)
    is_hospitalized = fields.Boolean('admitted to hospital', default=False,store=True)
    is_release_with_prescription = fields.Boolean('Release with prescription', default=False,store=True)
    price_total_medicine = fields.Float(compute='_compute_price_total_medicine', string="total price")
    gravity_disease = fields.Integer(compute='_compute_gravity_by_disease',store=True, string='Gravity')
    symptom_request_ids = fields.One2many(
        related='request_id.symptom_request_ids',
        readonly=True,
        string="Symptoms"
    )

    _sql_constraints = [
        ('treatment_duration_positive', 'CHECK(treatment_duration_days >= 0)',
         'Treatment duration must be a non-negative number.'),
    ]



    @api.depends('disease_id')
    def _compute_gravity_by_disease(self):
        self.ensure_one()
        self.gravity_disease = sum(self.disease_id.symptom_disease_ids.mapped('gravity'))

    @api.depends('consultation_line_ids')
    def _compute_price_total_medicine(self):
        for consultation in self:
            consultation.price_total_medicine = sum(self.consultation_line_ids.mapped('total_price'))

    @api.constrains('is_hospitalized', 'is_release_with_prescription')
    def _check_action_final(self):
        for record in self:
            if self.state == 'in_progress':
                if not record.is_hospitalized and not record.is_release_with_prescription:
                    raise ValidationError(
                        _('You must select at least one action: hospitalization or discharge with prescription.'))

    def action_release(self):
        if not self.disease_id:
            raise UserError(_('After your diagnosis you must choose the patient s disease'))
        self.ensure_one()
        self.is_release_with_prescription = True
        self.is_hospitalized = False
        self.treatment_duration_days = 0
        self.state = 'completed'



    def submit_hospitalized(self):
        self.ensure_one()
        if not self.disease_id:
            raise UserError(_('After your diagnosis you must choose the patient s disease'))
        if self.treatment_duration_days <= 0:
            raise UserError(_('Treatment duration must be a positive number.'))

        self.is_hospitalized = True
        self.is_release_with_prescription = False
        patient_hospitalized = self.env['hospital.hospitalized.patient']
        patient_hospitalized.sudo().create({
            'patient_id': self.patient_id.id,
            'disease_id': self.disease_id.id,
            'admission_date': date.today(),
            'nb_days_evaluation': self.treatment_duration_days,
            'state': 'admitted'
        })
        self.state = 'completed'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'current',
            'flags': {'reload': True},
        }



    def action_in_progress(self):
        self.ensure_one()
        self.state = 'in_progress'


    def action_cancel(self):
        self.ensure_one()
        self.state = 'canceled'