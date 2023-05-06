# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Car(models.Model):
    _name = "car.car"
    _description = "Car Model testing"

    car_name = fields.Char(string="Car Name")
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string="Doors Number")
    max_speed = fields.Integer(string="Max Speed")

    driver_id = fields.Many2one('res.partner', string="Driver")
    parking_id = fields.Many2one('parking.parking', string="Parking")
    features_ids = fields.Many2many('car.features')

    total_speed = fields.Integer(string="Total Speed", compute="get_total_speed")
    random_message = fields.Char(string="Random Message", compute="say_hi")


    status = fields.Selection([('new','New'),('used','Used'),('sold','Sold')], string="Status" , default="new")


    car_sequence = fields.Char(string='Sequence')


    @api.model
    def create(self, vals):
        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence') or _('New')
        result = super(Car, self).create(vals)
        return result    
    
    def say_hi(self):
        # print('driver_id', self.driver_id)
        # print('driver_id id', self.driver_id.id)
        # print('driver_id name', self.driver_id.name)     
        self.random_message = "Hi " + self.driver_id.name

    def get_total_speed(self):
        self.total_speed =  50 
    
    # def set_car_to_new(self):
    #     # print("-----------------------------")
    #     # print("hi")
    #     # print("-----------------------------")
    #     self.status = "New"

    def set_car_to_used(self):
        self.status = "used"
        
    def set_car_to_sold(self):
        self.status = "sold"


class Parking(models.Model):
    _name = "parking.parking"
    _description = "Parking Model testing"

    name = fields.Char(string="Parking Name")
    car_ids = fields.One2many('car.car', 'parking_id', string="Cars")

class CarFeatures(models.Model):
    _name = "car.features"
    _description = "Car Features Model testing"

    name = fields.Char(string="Feature Name")
    value = fields.Char(string="Feature Value")
    