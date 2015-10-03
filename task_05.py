#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability differences between strings and their cousin, the tuple."""


def flip_keys(to_flip):
    """list with its inner elements reversed

    Arguments:
        To flip a list

    Returns:
        The function should return the original list

    Examples:
        >>>print LIST
        [(3,2,1), 'cba']

    """

    counter = 0

    for item in to_flip:
        mylistvar = (item[::-1])
        to_flip[counter] = mylistvar
        counter += 1

    return to_flip
