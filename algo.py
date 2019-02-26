#!/usr/bin/env python3

from export_results import export_results
import os
from parse_input import parse_input
import sys
import basic_types
import time
from utils import print_, print_sec, print_ssec
import numpy as np
from basic_types import distance, Problem, Ride
import operator

# Main body of the hashcode algorithm

def compute_distances(curr_positions, veh_ids, rides, t):
    positions = {i: pos for i, pos in curr_positions.items()
                 if i in veh_ids}
    dists = {veh: {ride_id: None for ride_id in rides.keys()}
             for veh in veh_ids}

    if t == 0:
        veh_id = list(veh_ids)[0]
        dists_single_ride = {}
        for ride in rides.values():
            arrival_time = distance(positions[veh_id], ride.start)
            wait_time = np.max(ride.t_start - (t + arrival_time), 0)
            trip_time = ride.nom_val

            t_trip_finish = arrival_time + wait_time + trip_time
            dists_single_ride[ride.id] = t_trip_finish

        for veh_id in dists.keys():
            dists[veh_id] = dists_single_ride
    else:
        for veh_id in veh_ids:
            for ride in rides.values():
                arrival_time = distance(positions[veh_id], ride.start)
                wait_time = np.max(ride.t_start - (t + arrival_time), 0)
                trip_time = ride.nom_val

                t_trip_finish = arrival_time + wait_time + trip_time
                dists[veh_id][ride.id] = t_trip_finish

    return dists


# distance: (veh_id, ride_id)
def assign(curr_positions, veh_ids, rides, t):
    """Returns [(id pairs)], [distances]."""
    curr_dists = compute_distances(curr_positions, veh_ids, rides, t)
    # print("curr_dists: ", curr_dists)
    rideids_assigned = set()

    # out_dists = [0 for i in range(veh_ids)]
    # out_ids = [(0, 0) for i in range(veh_ids)]
    out_dists = []
    out_ids = []
    for veh_id in veh_ids:
        veh_rides = curr_dists[veh_id]
        veh_rides_sorted = dict(sorted(veh_rides.items(),
                                       key=operator.itemgetter(1)))
        for ride_id, dist in veh_rides_sorted.items():
            if ride_id not in rideids_assigned:
                rideids_assigned.add(ride_id)
                out_dists.append(dist)
                out_ids.append((veh_id, ride_id))
                break

    return out_dists, out_ids


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <path-to-input-file>".format(sys.argv[0]))
        exit(1)

    # Parse inputs
    input_f = sys.argv[1]
    # name of the current case
    fname = os.path.basename(input_f)
    print_sec("Running for case: {}".format(fname))

    if not os.path.isfile(input_f):
        raise FileNotFoundError(input_f)

    # Parse input - use serial form if it's there
    prob = parse_input(input_f)
    prob.kickstart()

    # Process
    print_ssec("computing...")
    out_ids, out_dists = assign(prob,
                                prob.curr_positions.keys(),
                                {ride.id: ride for ride in prob.rides}, 0)
    print("out_ids: ", out_ids)
    print("out_dists: ", out_dists)
    print_("compuations done.")

    # Export results
    outfile = "{}_{}".format(int(time.time()), fname)
    export_results(prob, outfile)

    print_("all done, exiting.")


if __name__ == "__main__":
    main()
