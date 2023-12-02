#!/usr/bin/env python3
import time

with open("input.txt", "r") as f:
    calibrations = f.readlines()


def sol1(calibrations):
    total = 0
    for cal in calibrations:
        buffer = ""
        for char in cal:
            if char.isdigit():
                buffer += char
                break
        for char in cal[::-1]:
            if char.isdigit():
                buffer += char
                break
        total += int(buffer)
    return total


def sol2(calibrations):
    total = 0
    for cal in calibrations:
        buffer = ""
        for char in cal:
            if char.isdigit():
                buffer += char
        total += int(buffer[0] + buffer[-1])
    return total


start1 = time.perf_counter()
print(sol2(calibrations))
stop1 = time.perf_counter()

start2 = time.perf_counter()
print(sol1(calibrations))
stop2 = time.perf_counter()

print(stop1-start1)
print(stop2-start2)
