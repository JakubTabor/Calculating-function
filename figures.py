import math


def area_sqare(a):
    return a * a


def area_rectangle(a, b):
    return a * b


def area_circle(r):
    return math.pi * r ** 2


def area_triangle(a, h):
    return 0.5 * a * h


def area_trapeze(a, b, h):
    return (a + b) / 2 * h
