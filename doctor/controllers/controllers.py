# -*- coding: utf-8 -*-
# from odoo import http


# class EtechAddons/hospitalProject/doctor(http.Controller):
#     @http.route('/etech_addons/hospital_project/doctor/etech_addons/hospital_project/doctor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etech_addons/hospital_project/doctor/etech_addons/hospital_project/doctor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('etech_addons/hospital_project/doctor.listing', {
#             'root': '/etech_addons/hospital_project/doctor/etech_addons/hospital_project/doctor',
#             'objects': http.request.env['etech_addons/hospital_project/doctor.etech_addons/hospital_project/doctor'].search([]),
#         })

#     @http.route('/etech_addons/hospital_project/doctor/etech_addons/hospital_project/doctor/objects/<model("etech_addons/hospital_project/doctor.etech_addons/hospital_project/doctor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etech_addons/hospital_project/doctor.object', {
#             'object': obj
#         })

