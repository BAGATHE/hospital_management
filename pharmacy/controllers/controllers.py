# -*- coding: utf-8 -*-
# from odoo import http


# class EtechAddons/hospitalProject/pharmacy(http.Controller):
#     @http.route('/etech_addons/hospital_project/pharmacy/etech_addons/hospital_project/pharmacy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etech_addons/hospital_project/pharmacy/etech_addons/hospital_project/pharmacy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('etech_addons/hospital_project/pharmacy.listing', {
#             'root': '/etech_addons/hospital_project/pharmacy/etech_addons/hospital_project/pharmacy',
#             'objects': http.request.env['etech_addons/hospital_project/pharmacy.etech_addons/hospital_project/pharmacy'].search([]),
#         })

#     @http.route('/etech_addons/hospital_project/pharmacy/etech_addons/hospital_project/pharmacy/objects/<model("etech_addons/hospital_project/pharmacy.etech_addons/hospital_project/pharmacy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etech_addons/hospital_project/pharmacy.object', {
#             'object': obj
#         })

