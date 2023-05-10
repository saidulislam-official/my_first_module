from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    message = fields.Char(string="Message")

    other_information = fields.Char(string="Other Info")
    
    message2 = fields.Char(string="Message 2")

    car_count = fields.Integer(string="Count", compute="get_car_count")

    def get_car_count(self):
        for rec in self:
            rec.car_count = self.env['fleet.vehicle'].search_count([('driver_id','=',self.id)])

    def get_cars(self):
        self.ensure_one()
        return{
            'type':'ir.actions.act_window',
            'name':'Cars',
            'view_mode':'tree',
            'res_model':'fleet.vehicle',
            'domain':[('driver_id','=',self.id)],
            'context':"{'create': False}",
        }
    