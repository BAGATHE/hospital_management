# -*- coding: utf-8 -*-
# from odoo import http


# class EtechAddons/hospitalProject/patientPortal(http.Controller):
#     @http.route('/etech_addons/hospital_project/patient_portal/etech_addons/hospital_project/patient_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etech_addons/hospital_project/patient_portal/etech_addons/hospital_project/patient_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('etech_addons/hospital_project/patient_portal.listing', {
#             'root': '/etech_addons/hospital_project/patient_portal/etech_addons/hospital_project/patient_portal',
#             'objects': http.request.env['etech_addons/hospital_project/patient_portal.etech_addons/hospital_project/patient_portal'].search([]),
#         })

#     @http.route('/etech_addons/hospital_project/patient_portal/etech_addons/hospital_project/patient_portal/objects/<model("etech_addons/hospital_project/patient_portal.etech_addons/hospital_project/patient_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etech_addons/hospital_project/patient_portal.object', {
#             'object': obj
#         })

