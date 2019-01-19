#!/usr/bin/env python3

# A complete build that you could race with
class Build:
    def __init__(self, driver, vehicle, tires, glider):
        self.driver = driver
        sefl.vehicle = vehicle
        self.tires = tires
        self.glider = glider

# A part of a build
class Component:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    # given the stat_name (as a string), this returns a float that is the value
    # of that stat
    def get_stat(self, stat_name):
        return self.stats[stat_name]

    # these functions are for customizing what print() does with this class
    def __str__(self):
        return self.name + " " + str(list(self.stats.values()))
    def __repr__(self):
        return str(self)

# The four kinds of components of a build
class Driver(Component):
    pass
class Vehicle(Component):
    pass
class Tires(Component):
    pass
class Glider(Component):
    pass
