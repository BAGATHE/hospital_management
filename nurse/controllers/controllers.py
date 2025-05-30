# -*- coding: utf-8 -*-
# from odoo import http


# class EtechAddons/hospitalProject/nurse(http.Controller):
#     @http.route('/etech_addons/hospital_project/nurse/etech_addons/hospital_project/nurse', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etech_addons/hospital_project/nurse/etech_addons/hospital_project/nurse/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('etech_addons/hospital_project/nurse.listing', {
#             'root': '/etech_addons/hospital_project/nurse/etech_addons/hospital_project/nurse',
#             'objects': http.request.env['etech_addons/hospital_project/nurse.etech_addons/hospital_project/nurse'].search([]),
#         })

#     @http.route('/etech_addons/hospital_project/nurse/etech_addons/hospital_project/nurse/objects/<model("etech_addons/hospital_project/nurse.etech_addons/hospital_project/nurse"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etech_addons/hospital_project/nurse.object', {
#             'object': obj
#         })

