# Contains the basic types for the HashCode Problem
from utils import print_
import numpy as np

class Point(object):
    def __init__(self, r=0, c=0):
        self.r = r
        self.c = c

    def __repr__(self):
        msg = "({},{})".format(self.r, self.c)
        return msg


def distance(p1, p2):
    return (np.abs(p1.r - p2.r) + np.abs(p1.c - p2.c))


class Ride(object):
    def __init__(self, start=Point(), end=Point(),
                 t_start=-1, t_end=-1, _id=-1):
        self.id = _id
        self.start = start
        self.end = end
        self.t_start = t_start
        self.t_end = t_end

        # Nominal value of ride (no bonus)
        self.nom_val = distance(self.start, self.end)
        self.max_val = distance(self.start, self.end)

    def __repr__(self):
        msg =  "[{}]\n".format(self.id)
        msg += "  * start: {}\n".format(self.start)
        msg += "  * end: {}\n".format(self.end)
        msg += "  * t_start: {}\n".format(self.t_start)
        msg += "  * t_end: {}\n\n".format(self.t_end)

        return msg

class Problem:
    """Container for the whole problem."""

    def __init__(self):
        pass

        # Totals
        self.R = -1
        self.C = -1
        self.F = -1
        self.N = -1
        self.B = -1
        self.T = -1

        self.rides = []

        # index is the CAR ID, contains the rides for each car
        # Example
        # [[0, ],
        # [[2, 1]]
        # self.assigns = [[Ride(Point(), Point(), 0, 0, 0), ],
        #                 [Ride(Point(), Point(), 0, 0, 2),
        #                  Ride(Point(), Point(), 0, 0, 1)], ]
        self.assigns = []
        self.curr_positions = []

    def kickstart(self):
        self.curr_positions = [Point() for i in range(self.F)]
        self.assigns = [Ride() for i in range(self.F)]
