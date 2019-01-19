#!/usr/bin/env python3
import sys
import reader

def main(args):
    # parse the arguments
    # args[0] is the name of this file
    # args[1] is the first argument (the weights file)
    if len(args) < 2 or args[1] == "--help":
        print("Usage: {} <weights_file>".format(args[0]))
        return
    weights_file = args[1]

    # read in the data we need
    weights = reader.read_weights(weights_file)
    drivers = reader.read_data("data/drivers.csv")
    vehicles = reader.read_data("data/vehicles.csv")
    tires = reader.read_data("data/tires.csv")
    gliders = reader.read_data("data/gliders.csv")

    # TODO: filter out duplicates
    # TODO: choose the best builds and print them out

if __name__ == "__main__":
    main(sys.argv)
