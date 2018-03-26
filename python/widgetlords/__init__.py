from ctypes import *

__all__ = []

widgetlords = cdll.LoadLibrary('libwidgetlords.so')

def steinhart_hart(r_room: float, r_beta: float, counts_range: int, counts: int):
    return widgetlords.widgetlords_steinhart_hart(r_room, r_beta, counts_range, counts)
__all__.append('steinhart_hart')

def counts_to_value(counts: int, zero_counts: int, range_counts: int, zero: float, range: float):
    return widgetlords.widgetlords_counts_to_value(counts, zero_counts, range_counts, zero, range)
__all__.append('counts_to_value')