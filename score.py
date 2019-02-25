#!/usr/bin/env python

import argparse

from parse_input import parse_input
from basic_types import Ride
from basic_types import distance

import numpy as np


def parse_output(self, filename):
    assigns = []
    with open(filename) as f:
        for line in f:
            num_assigns, *ride_ids = line.split()
            ride_ids = [Ride(_id=int(i)) for i in ride_ids]
            assigns.append(ride_ids)
    self.assigns = assigns


def run(self):
    self.is_completed = np.zeros((self.N,), dtype=bool)
    self.curr_rides = [None for i in range(self.F)]
    self.launch_times = [None for i in range(self.F)]
    for current_time in range(self.T):
        # -----------------------------------------------------------------------------
        # Assignment: launching all cars to the next ride
        for f in range(self.F):
            # XXX: Write assignment algorithm here!

            assigns = self.assigns[f]
            for assign in assigns:
                if self.is_completed[assign.id]:
                    continue

                ride = self.rides[assign.id]

                curr_ride = self.curr_rides[f]

                # check if already assigned or not
                if curr_ride is None or self.is_completed[curr_ride.id]:
                    self.curr_rides[f] = ride            # next job
                    self.launch_times[f] = current_time  # launch to go to the starting point
        # -----------------------------------------------------------------------------

        # -----------------------------------------------------------------------------
        # Run one step
        for f in range(self.F):
            curr_ride = self.curr_rides[f]
            launch_time = self.launch_times[f]
            # to get to the start point of the ride
            required_time = distance(curr_ride.start, self.curr_positions[f])

            is_arrived = (current_time - launch_time) >= required_time

            # if arrived, curr_positions is updated
            if is_arrived:
                self.curr_positions[f] = curr_ride.start

            is_completed = (current_time - launch_time) >= (required_time + curr_ride.nom_val)

            # if completed, curr_positions is updated
            if is_completed:
                self.is_completed[next_ride.id] = True
                self.curr_positions[f] = curr_ride.end
        # -----------------------------------------------------------------------------


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
# parser.add_argument('input_file')
# parser.add_argument('output_file')
args = parser.parse_args()

args.input_file = 'data/a_example.in'
args.output_file = 'data/a_example.out'

prob = parse_input(args.input_file)
print(prob)

parse_output(prob, args.output_file)

run(prob)
