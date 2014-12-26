#!/usr/bin/env python

__usage__ = """
NAME
        uuid64 - generate a 64bit UUID

SYNOPSIS
        uuid64 [--help]
        uuid64 [int|hex|bin|oct]

DESCRIPTION
        This is a simple script that generates a 64bit UUID. The normal type of
        UUID (e.g. those available in the uuid module) are 128bit, which
        provides substantially greater ability to avoid collision between
        generated values. However, it is sometimes convenient to have a smaller
        UUID, e.g. if the number of generated values is not terribly large or
        will not be generated in large batches. Or, perhaps, due to a lack of
        support for 128bit integers.

        The algorithm used to generate these UUIDs is very simple. The UUID
        consists of two 32bit parts. The first part is base upon the current
        time (seconds since the beginning of epoch). When UUIDs are not
        generated in batches, i.e. all at the same time, the time acts as an
        incrementing value so that UUID generate many seconds apart are almost
        certain to be different (note that clock timing on different machines
        means that this is not a guarantee).

        The second part is a 32bit random number taken from the system that the
        script is running on, e.g. on linux the value is taken from
        /dev/urandom rather than a pseudo-random generator.

OPTIONS
        -h, --help
            Print out this documentation

        int
            This is the default format. The UUID is returned as an integer.

        hex
            The UUID is returned in a hexidecimal representation.

        bin
            The UUID is returned in a binary representation.

        hex
            The UUID is returned in an hexidecimal representation.

"""

import __builtin__
import argparse
import random
import sys
import time

def int():
    """Return UUID as integer"""
    base = __builtin__.int(time.time()) << 32
    rand = random.SystemRandom().getrandbits(32)
    return base + rand


def hex():
    """Return UUID as hexidecimal"""
    return __builtin__.hex(int())[2:-1]


def bin():
    """Return UUID as binary"""
    return __builtin__.bin(int())[2:]


def oct():
    """Return UUID as octodecimal"""
    return __builtin__.oct(int())[:-1]


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('format',
            nargs='?',
            choices=('int', 'hex', 'bin', 'oct'),
            default='int')
    parser.add_argument('-h', '--help',
            action='store_true')

    args = parser.parse_args(argv)

    if args.help:
        print(__usage__)
        return

    print(getattr(sys.modules[__name__], args.format)())

if __name__ == "__main__":
    main()
