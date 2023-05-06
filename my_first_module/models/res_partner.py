from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    message = fields.Char(string="Message")

    other_information = fields.Char(string="Other Info")
    
    message2 = fields.Char(string="Message 2")