"""Tiny calculator used to demonstrate CI analysis."""
import statistics


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mean(values):
    return float(statistics.mean(values))
