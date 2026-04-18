"""
Complete the function which will return the area of a circle with the given radius.

Returned value is expected to be accurate up to tolerance of 0.01.

If the radius is not positive, raise ValueError.

Example:

circle_area(43.2673)      # returns 5881.248  (± 0.01)
circle_area(68)           # returns 14526.724 (± 0.01)
circle_area(0)            # raises ValueError
circle_area(-1)           # raises ValueError
"""

import math

def circle_area(r):
    if r <= 0:
        raise ValueError("Radius must be positive")
    area = math.pi * r * r
    return round(area, 3)


# Teste

print(circle_area(43.2673))  # 5881.248
print(circle_area(68))        # 14526.724