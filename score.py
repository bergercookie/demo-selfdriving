#!/usr/bin/env python

import argparse

from parse_input import parse_input
from basic_types import Ride
from basic_types import distance
from algo import compute_distances
from algo import assign

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
    rides_remaining = {ride.id: ride for ride in self.rides}

    self.score = 0

    # tasks: [(car_id, ride_id), ...]
    car_ids = list(range(self.F))
    positions = {car_id: self.curr_positions[car_id] for car_id in car_ids}
    distances, tasks = assign(positions, car_ids, rides_remaining, 0)

    import heapq

    heap = []
    for i in range(len(distances)):
        heapq.heappush(heap, (distances[i], tasks[i]))
        rides_remaining.pop(tasks[i][1])

    import tqdm
    pbar = tqdm.tqdm(total=len(rides_remaining))

    while heap:
        ending_list = []
        task_list = []

        ending, task = heapq.heappop(heap)
        ending_list.append(ending)
        task_list.append(task)
        while heap and heap[0][0] == ending:
            ending, task = heapq.heappop(heap)
            ending_list.append(ending)
            task_list.append(task)

        for ending, task in zip(ending_list, task_list):
            car_id, ride_id = task
            ride = self.rides[ride_id]

            self.curr_positions[car_id] = ride.end

            if ending < ride.t_end:
                self.score += ride.nom_val

            if (ending - ride.nom_val) == ride.t_start:
                self.score += self.B

            if len(rides_remaining) > 0:
                positions = {car_id: self.curr_positions[car_id]}
                distance, task = assign(
                    positions, [car_id], rides_remaining, ending)
                heapq.heappush(heap, (distance[0], task[0]))
                rides_remaining.pop(task[0][1])

        pbar.update(n=len(self.rides) - len(rides_remaining) - pbar.n)

    return self.score


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
args = parser.parse_args()

# args.input_file = 'data/a_example.in'
# args.input_file = 'data/b_should_be_easy.in'
args.input_file = 'data/c_no_hurry.in'

prob = parse_input(args.input_file)
prob.kickstart()
print(prob)

score = run(prob)
print(score)
