"""
A tire size is written in the format "205/55R16" where:

205 → tire width in millimeters
55 → aspect ratio (sidewall height as a percentage of width)
16 → rim diameter in inches
The construction code between aspect ratio and rim diameter can be R, ZR, B, or D. Given a tire size string and a
distance in kilometers, return the number of rotations the tire makes.

Function signature:

def tire_rotations(tire_size: str, distance_km: float) -> float:
Examples:

tire_rotations("205/55R16", 110) ≈ 55410.8047
tire_rotations("185/65ZR15", 900) ≈ 460947.5423
tire_rotations("225/45B17", 0) == 0.0
Notes:

Use π = math.pi
1 inch = 25.4 mm
"""

from math import pi
import re

def tire_rotations(tire_size: str, distance_km: float) -> float:
    match = re.match(r'(\d+)/(\d+)[A-Z]+(\d+)', tire_size)

    if not match:
        return 0.0

    width = int(match.group(1))
    aspect = int(match.group(2))
    rim = int(match.group(3))

    diameter_mm = rim * 25.4 + 2 * width * aspect / 100

    return (distance_km * 1_000_000) / (pi * diameter_mm)

# Teste

print(tire_rotations("205/55R16", 110))
print(tire_rotations("185/65ZR15", 900))
print(tire_rotations("225/45B17", 0))
print(tire_rotations("195/65R15", 10))