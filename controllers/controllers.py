# -*- coding: utf-8 -*-
from openerp import http

# class Addons\maplepick(http.Controller):
#     @http.route('/addons\maplepick/addons\maplepick/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons\maplepick/addons\maplepick/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons\maplepick.listing', {
#             'root': '/addons\maplepick/addons\maplepick',
#             'objects': http.request.env['addons\maplepick.addons\maplepick'].search([]),
#         })

#     @http.route('/addons\maplepick/addons\maplepick/objects/<model("addons\maplepick.addons\maplepick"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons\maplepick.object', {
#             'object': obj
#         })