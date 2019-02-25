#!/usr/bin/env python

import argparse

from parse_input import parse_input

import numpy as np


def parse_output(self, filename):
    assigns = []
    with open(filename) as f:
        for line in f:
            num_assigns, *ride_ids = line.split()
            ride_ids = [int(i) for i in ride_ids]
            assigns.append(ride_ids)
    self.assigns = assigns


def run(self):
    self.positions = np.zeros((self.F, 2), dtype=int)
    self.goals_and_
    for t in range(self.T):
        for f in range(self.F):
            assigns = self.assigns[f]
            for assign in assigns:
                ride = self.rides[assign.id]
                ride = self.rides[assign]
                import ipdb; ipdb.set_trace()  # NOQA


# def score(self):
#     completed = []
#     with_bonus = []
#
#     for t in range(self.T):


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
