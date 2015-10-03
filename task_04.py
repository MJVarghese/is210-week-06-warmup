#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping"""


def process_data(data):
    """The sum and mean of the data

    arguments:
        myave: will return mean of sum of the given set

        loop: every item in the set is being added to mysum

    returns:
        will return sum and mean of the set as a tuple

    examples:
        process_data([1,2,3])
        >>>(6, 2.0)
    """

    mysum = 0

    for mynum in data:
        mysum += mynum

        myave = mysum/float(len(data))

    return mysum, myave
