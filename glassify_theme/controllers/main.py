import base64

from odoo import http
from odoo.http import request


class ThemeLiquidGlassController(http.Controller):

    @http.route("/glassify_theme/logo", type="http", auth="user")
    def theme_logo(self, **kw):
        company = request.env.company
        if company.theme_logo:
            image = base64.b64decode(company.theme_logo)
            return request.make_response(
                image, [("Content-Type", "image/png")]
            )
        return request.redirect("/web/binary/company_logo")
