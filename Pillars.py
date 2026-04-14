"""
There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same.
Your function accepts three arguments:

number of pillars (≥ 1);
distance between pillars (10 - 30 meters);
width of the pillar (10 - 50 centimeters).
Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last
pillar).
"""


def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    dist_cm = dist * 100
    num_gaps = num_pill - 1
    total_gap_distance = num_gaps * dist_cm
    total_width_internal = (num_pill - 2) * width
    return total_gap_distance + total_width_internal

# Teste

print(pillars(1, 10, 10))  # 0
print(pillars(2, 10, 10))  # 1000
print(pillars(3, 10, 10))  # 2010
print(pillars(5, 20, 25))  # 8075

