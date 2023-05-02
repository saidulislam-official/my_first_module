# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Car(models.Model):
    _name = "car.car"
    _description = "Car Model testing"

    car_name = fields.Char(string="Name")
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string="Doors Number")
    max_speed = fields.Integer(string="Max Speed")
