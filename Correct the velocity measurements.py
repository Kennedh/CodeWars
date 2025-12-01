"""
Overview
You, a police officer, have been tasked with catching speeding drivers on your town's roads. You were given access to
the following equipment:

A clock
A LIDAR gun which tells you the distance to (but not speed of) a given object
As you set about your duties, your first thought was to measure a car's distance from yourself twice, divide by the time
between measurements, and calculate its speed that way. Simple physics! Two crafty criminals, however, challenge you in court:

Criminal #1: But you were walking toward me at the time! That means you actually measured the sum of our speeds, not
just mine!

Criminal #2: But I wasn't driving directly toward you! Your measurement is subject to cosine error!

The judge agrees. Using just distance-to-target over time is insufficient if the one doing the measuring is moving, or
if the target's trajectory is not directly towards/away from the observer. Your department begrudgingly shells out for
another two pieces of equipment:

A compass
A GPS
You now have what you need to catch these dastardly, mathematically-adept speedsters.

The Task
Given two sets of readings from the equipment specified above, calculate the speed of the target.

Inputs
Two dictionaries in the following form

reading = {
  'time': A float, the time in seconds since some arbitrary epoch when the reading was taken
  'distance': A float, the distance in meters to the target of your LIDAR
  'angle': A float, the angle in radians between the positive x-axis and the target relative to the observer*
  'position': A 2-tuple of floats, the observer's coordinates in meters from some arbitrary origin
}
Outputs
The target's speed in m/s

Example
Let's say you're in your police car at (0, 0) and your clock reads 0s. You see a (putative) speedster north of you,
along the positive Y axis 30m away. Taking a reading of your instruments, you see:

reading_a = {
  'time': 0,
  'distance': 30,
  'angle': pi/2,
  'position': (0, 0)
}
after 5 seconds, your squad car has rolled 10m to the west, putting you at (-10, 0). The offender is now due east and
50m away; your measurements are:

reading_b = {
  'time': 5,
  'distance': 50,
  'angle': 0,
  'position': (-10, 0)
}
From the information above, you're able to deduce that the other party moved 50m in 5s, and so they were moving at
10m/s.

Constraints/assumptions/notes
* In other words, if you (the observer) are looking along the positive x-axis, how many radians must you turn
anti-clockwise until you are facing the target? This will always be 0 <= angle < 2π.
The world is a 2D plane (harharhar).
Time between measurements will always be >= 0.1s, with the second reading coming later than the first.
The target and observer will always be moving at <= 100m/s relative to the world.
Results are validated +-0.01m/s.
"""
import math

def calculate_speed(reading_a, reading_b):
    x_obs, y_obs = reading_a['position']
    dist = reading_a['distance']
    ang = reading_a['angle']
    x_rel = dist * math.cos(ang)
    y_rel = dist * math.sin(ang)

    x_target_a = x_obs + x_rel
    y_target_a = y_obs + y_rel

    x_obs, y_obs = reading_b['position']
    dist = reading_b['distance']
    ang = reading_b['angle']
    x_rel = dist * math.cos(ang)
    y_rel = dist * math.sin(ang)

    x_target_b = x_obs + x_rel
    y_target_b = y_obs + y_rel

    delta_x = x_target_b - x_target_a
    delta_y = y_target_b - y_target_a

    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

    time_delta = reading_b["time"] - reading_a["time"]

    return distance / time_delta

# Teste

print(calculate_speed({'time': 0, 'distance': 10, 'angle': 0, 'position': (0, 0)},
{'time': 1, 'distance': 9, 'angle': 0, 'position': (0, 0)}))