from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    theme_logo = fields.Binary(string="Navbar Logo", attachment=True)
