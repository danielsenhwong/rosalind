#!/usr/bin/python
# -*- coding: utf-8
""" problem fibd
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th\
        month if all rabbits live for m months.
"""

from rosalind import *

def dyn_fib(test=False):
    """ Recurrence relation """
    if not test:
        data = import_data(problem='fibd')

        fib_consts = data[0].split()
    else:
        fib_consts = [6, 3]

    duration = int(fib_consts[0])
    max_age = int(fib_consts[1])

    population = [0] * max_age # newborns, mature, elderly
    population[0] = 1 # start with newborn pair

    for i in range(duration-1):
        newborns = sum(population[1:])
        # new newborns, old newborns mature, we stop keeping track of elderly.
        population = [newborns] + population[:max_age-1]
    return sum(population)

