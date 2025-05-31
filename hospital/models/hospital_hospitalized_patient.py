from odoo  import fields, models,api

class HospitalHospitalizedPatient(models.Model):
    _name = 'hospital.hospitalized.patient'
    _description = 'Hospital Hospitalized Patient'

    admission_date = fields.Date(string="admission date", required=True)
    nb_days_evaluation = fields.Integer(string="number of days evaluation", required=True,default=1)
    state = fields.Selection(string="Patient Status",
        selection=[
            ('admitted', 'Admitted'),
            ('under_treatment', 'Under Treatment'),
            ('in_remission', 'In Remission'),
            ('discharged', 'Discharged')
        ],
        default='admitted',
        help="Workflow: Admitted -> Under Treatment -> In Remission -> Ready for Discharge -> Discharged"
    )
    patient_id = fields.Many2one('hospital.patient',required=True, ondelete='cascade',string='patient')
    disease_id = fields.Many2one('hospital.disease',required=True,ondelete='cascade',string='disease')
