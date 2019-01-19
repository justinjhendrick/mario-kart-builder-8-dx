#!/usr/bin/env python3
import csv
from definitions import *

# This module defines functions for reading the csvs and the weight files

# read the weights file. Expected input is like this
# ```
# stat1: value
# stat2: value
# stat3: value
# ```
# where value is a number
def read_weights(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            key, value = line.split(':')
            # strip removes leading and trailing whitespace
            result[key.strip()] = float(value.strip())
    return result


# Reads the csv file at `filename` and returns a list of Components
# This expects csv like this
#
# ```
# ,Kind,stat1,stat2
# 0,name_a,1.0,-1.0
# 1,name_b,1.0,-1.0
# 2,name_c,1.0,-1.0
# ```
# where Kind is one of "Vehicle", "Driver", "Tire", or "Glider"
def read_data(filename):

    # a helper function to create each kind of component
    def create_component(kind, name, stats):
        if kind == "Vehicle":
            return Vehicle(name, stats)
        elif kind == "Driver":
            return Driver(name, stats)
        elif kind == "Tire":
            return Tires(name, stats)
        elif kind == "Glider":
            return Glider(name, stats)
        return None

    result = []
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        headers = []
        first = True
        for row in spamreader:
            # the first row contains the names of all the columns
            if first:
                headers = row
                first = False
                continue

            # build the stats
            stats = {}
            for i, elem in enumerate(row):
                if i <= 1:
                    # ignore the row number and the name
                    # because they're not stats
                    continue
                stats[headers[i]] = float(elem)

            kind = headers[1]
            name = row[1]
            result.append(create_component(kind, name, stats))
    return result

def _test():
    weights = read_weights('example_weights.txt')
    print(weights)
    parsed = read_data('data/tires.csv')
    for v in parsed:
        print(v)

if __name__ == "__main__":
    # this code will be run if this file is invoked, like `python3 reader.py`
    _test()
