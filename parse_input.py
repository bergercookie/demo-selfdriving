from basic_types import Problem, Ride, Point
from utils import print_, print_sec, print_ssec, sep, ssep


def parse_input(f_in: str):
    """Parse the input file, fill and return the `Problem` class instance."""
    print_ssec("parsing input...")

    # Read all contents - line by line
    with open(f_in, 'r') as f:
        conts = [[int(s) for s in i.rstrip().split()] for i in f.readlines()]

    # Remove last line if empty
    if conts[-1] == '':
        conts = conts[:-1]

    prob = Problem()

    # Total values
    prob.R, prob.C, prob.F, prob.N, prob.B, prob.T = conts[0]

    # Get rest of items - N Rides
    for line in range(1, prob.N + 1):
        c = conts[line]
        _id = line - 1
        line += 1
        start = Point(c[0], c[1])
        end = Point(c[2], c[3])
        t_start, t_end = c[4], c[5]
        prob.rides.append(Ride(start, end, t_start, t_end, _id))

    # Print stuff out
    print_ssec("Inputs: ")
    print("* R: {} rows".format(prob.R))
    print("* C: {} columns".format(prob.C))
    print("* F: {} vehicles/fleet".format(prob.F))
    print("* N: {} rides".format(prob.N))
    print("* B: {} bonus".format(prob.B))
    print("* T: {} simulation steps/turns".format(prob.T))
    print()
    # print_("R: {}| C: {}| F: {}| N: {}| B: {}| T: {}".format(
    #     prob.R, prob.C, prob.F, prob.N, prob.B, prob.T
    # ))

    print("rides:\n", prob.rides)
    print_("parsed input successfully")
    return prob

