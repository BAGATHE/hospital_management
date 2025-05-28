# -*- coding: utf-8 -*-
# from odoo import http


# class EtechAddons/hospitalProject/hospitalDisease(http.Controller):
#     @http.route('/etech_addons/hospital_project/disease_management/etech_addons/hospital_project/disease_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etech_addons/hospital_project/disease_management/etech_addons/hospital_project/disease_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('etech_addons/hospital_project/disease_management.listing', {
#             'root': '/etech_addons/hospital_project/disease_management/etech_addons/hospital_project/disease_management',
#             'objects': http.request.env['etech_addons/hospital_project/disease_management.etech_addons/hospital_project/disease_management'].search([]),
#         })

#     @http.route('/etech_addons/hospital_project/disease_management/etech_addons/hospital_project/disease_management/objects/<model("etech_addons/hospital_project/disease_management.etech_addons/hospital_project/disease_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etech_addons/hospital_project/disease_management.object', {
#             'object': obj
#         })

