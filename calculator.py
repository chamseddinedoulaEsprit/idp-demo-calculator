"""Tiny calculator used to demonstrate CI analysis."""
import statistics


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('division by zero is not allowed')
    return a / b


def mean(value):
    return float(statistics.mean(value))
