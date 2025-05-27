# -*- coding: utf-8 -*-
# from odoo import http


# class EtechAddons/hospitalProject/hospital(http.Controller):
#     @http.route('/etech_addons/hospital_project/hospital/etech_addons/hospital_project/hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etech_addons/hospital_project/hospital/etech_addons/hospital_project/hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('etech_addons/hospital_project/hospital.listing', {
#             'root': '/etech_addons/hospital_project/hospital/etech_addons/hospital_project/hospital',
#             'objects': http.request.env['etech_addons/hospital_project/hospital.etech_addons/hospital_project/hospital'].search([]),
#         })

#     @http.route('/etech_addons/hospital_project/hospital/etech_addons/hospital_project/hospital/objects/<model("etech_addons/hospital_project/hospital.etech_addons/hospital_project/hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etech_addons/hospital_project/hospital.object', {
#             'object': obj
#         })

