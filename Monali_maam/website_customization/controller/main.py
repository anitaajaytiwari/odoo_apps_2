# -*- coding: utf-8 -*-
import odoo.http as http

class CustomTemplate(http.Controller):
     @http.route('/custom/url', type='http', auth='user', website=True)
     def show_custom_webpage(self, **kw):
          print ("\n\n..................................")
          return http.request.render('website_customization.custom_template_id', {})

     @http.route('/website_partner', type='http', auth='user', website=True)
     def show_partner_details_webpage(self, **kw):
          print ("\n\n.........partner.........................")
          return http.request.render('website_customization.partner_details', {})

