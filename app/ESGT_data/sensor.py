##!/usr/bin/python
'''
File name: sensor.py
Author: Kairi Kozuma, Boa-Lin Lai
Date created: 02/17/2017
Date last modified: 02/28/2017
Python Version: 3.6.0
'''
import json

class Sensor(object):
    def __init__(self, name, serialnumber, units, conversion_func):
        #
        self.name = name
        self.serialnumber = serialnumber
        self.units = units # String in units
        self.conv_func = conversion_func # Function to convert value to meaningful units
        self.value = 0.0 # Default value is 0
    def set_value(self, value):
        self.value = value
    def to_json_string(self):
        value_in_units = self.conv_func(self.value) # Convert to meaningful units
        data = dict(
            name=self.name,
            serialnumber=self.serialnumber,
            units=self.units,
            value=value_in_units
        )
        return json.dumps(data)

