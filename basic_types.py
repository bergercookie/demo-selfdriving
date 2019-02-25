# Contains the basic types for the HashCode Problem
from utils import print_

class Point(object):
    def __init__(self, r=-1, c=-1):
        self.r = r
        self.c = c

    def __repr__(self):
        msg = "({},{})".format(self.r, self.c)
        return msg


class Ride(object):
    def __init__(self, start, end, t_start, t_end):
        self.start = start
        self.end = end
        self.t_start = t_start
        self.t_end = t_end

    def __repr__(self):
        msg =  "* start: {}\n".format(self.start)
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

    # TODO - Add viewers to the data
