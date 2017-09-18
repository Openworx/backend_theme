# -*- coding: utf-8 -*-
from odoo.http import Controller, request, route
from werkzeug.utils import redirect


class DasboardBackground(Controller):
    """Dashboard background controller"""

    @route(['/dashboard-background'], type='http',
                auth='user', website=False)
    def dashboard(self, **post):
        """Redirects to the background image"""
        parameters_model = request.env['ir.config_parameter']
        image = parameters_model.search([('key', '=', 'dashboard_background')],
                                        limit=1).value
        return redirect(image)
