# -*- coding: utf-8 -*-
# from odoo import http


# class /home/ud/odoo/custom/testodoomodule(http.Controller):
#     @http.route('//home/ud/odoo/custom/testodoomodule//home/ud/odoo/custom/testodoomodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/ud/odoo/custom/testodoomodule//home/ud/odoo/custom/testodoomodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/ud/odoo/custom/testodoomodule.listing', {
#             'root': '//home/ud/odoo/custom/testodoomodule//home/ud/odoo/custom/testodoomodule',
#             'objects': http.request.env['/home/ud/odoo/custom/testodoomodule./home/ud/odoo/custom/testodoomodule'].search([]),
#         })

#     @http.route('//home/ud/odoo/custom/testodoomodule//home/ud/odoo/custom/testodoomodule/objects/<model("/home/ud/odoo/custom/testodoomodule./home/ud/odoo/custom/testodoomodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/ud/odoo/custom/testodoomodule.object', {
#             'object': obj
#         })
