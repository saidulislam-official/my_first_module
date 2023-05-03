# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
   
    def get_total_speed(self):
        self.total_speed = 100
    
    

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
    