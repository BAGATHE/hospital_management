from odoo import http
from odoo.http import request
from ..utils.validation import validate_portal_request_data
from odoo.exceptions import ValidationError


def _handle_create_request(patient, post):
    request_date = post.get('request_date')
    doctor_id = post.get('doctor_id')
    symptom_ids = request.httprequest.form.getlist('symptom_ids')

    validate_portal_request_data(request_date, doctor_id, symptom_ids)

    symptom_requests = [(0, 0, {'symptom_id': int(s_id)}) for s_id in symptom_ids]
    patient_portal_request = request.env['hospital.request']
    patient_portal_request.sudo().create({
        'request_date': request_date,
        'patient_id': patient.id,
        'doctor_id': int(doctor_id),
        'state':'pending',
        'symptom_request_ids': symptom_requests,
    })

    request.session['request_success'] = True


class PatientPortal(http.Controller):

    def __init__(self):
        pass

    @http.route('/my/requests', type='http', auth='user', website=True)
    def my_requests(self, **kw):
        patient = request.env['hospital.patient'].sudo().search([('user_id', '=', request.uid)], limit=1)
        requests = request.env['hospital.request'].sudo().search([('patient_id', '=', patient.id)])
        return request.render('patient_portal.portal_my_requests', {
            'requests': requests,
            'patient': patient,
        })



    @http.route('/my/requests/new', type='http', auth='user', website=True, methods=["GET", "POST"])
    def new_request(self, **post):
        patient = request.env['hospital.patient'].sudo().search([('user_id', '=', request.uid)], limit=1)
        symptoms = request.env['hospital.symptom'].sudo().search([])
        doctors = request.env['hospital.doctor'].sudo().search([])

        if http.request.httprequest.method == 'POST':
            try:
                print("avant appel")
                _handle_create_request(patient, post)
                return request.redirect('/my/requests')

            except ValidationError as e:
                print("Validation error")
                return request.render('patient_portal.portal_new_request', {
                    'patient': patient,
                    'symptoms': symptoms,
                    'doctors': doctors,
                    'error': str(e),
                    'post': post,
                })
        print("get get get request")
        return request.render('patient_portal.portal_new_request', {
            'patient': patient,
            'symptoms': symptoms,
            'doctors': doctors,
        })
