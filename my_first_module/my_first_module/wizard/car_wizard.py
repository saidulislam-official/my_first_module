from odoo import models, fields, api, _


class CarWizard(models.TransientModel):
    _name = 'car.wizard'
    _description = 'Car Wizard'

    horse_power_plus = fields.Integer(string="Horse Power")


    def add_horse_power(self):
        # print("---**********---")
        # print("We are on the wizard")
        # print("---**********---")
        print("**** Test From Wizard****")
        print('car_id', self.env.context.get('active_id'))
        print('horse power', self.horse_power_plus)

        self.env['car.car'].browse(self.env.context.get('active_id')).write({
            'horse_power': self.horse_power_plus
        })