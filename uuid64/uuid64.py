import __builtin__
import random
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
