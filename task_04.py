#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping"""


def process_data(data):
    """The sum and mean of the data

    arguments:
        myave: returns mean of sum of the given dataset

        for loop: every item (mynum) in the dataset is being added to mysum (0)

    returns:
        returns sum of dataset and mean of the dataset as a tuple

    examples:
        process_data([1,2,3])
        >>>(6, 2.0)
    """

    mysum = 0

    for mynum in data:
        mysum += mynum

        myave = mysum/float(len(data))

    return mysum, myave
