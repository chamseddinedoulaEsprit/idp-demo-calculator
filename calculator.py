"""Tiny calculator used to demonstrate CI analysis."""
import numpy as np


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def mean(values):
    return float(np.mean(values))
