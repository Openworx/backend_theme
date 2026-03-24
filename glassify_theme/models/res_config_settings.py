from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    theme_logo = fields.Binary(
        string="Navbar Logo",
        related="company_id.theme_logo",
        readonly=False,
    )
