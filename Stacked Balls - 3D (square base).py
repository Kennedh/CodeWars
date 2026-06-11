"""
Background
I have stacked some cannon balls in a square pyramid.

Like this,

cannon balls
Kata Task
Given the number of layers of my stack, what is the total height?

Return the height as multiple of the ball diameter.

Example
The image above shows a stack of 4 layers.

Notes
layers >= 0
approximate answers (within 0.001) are good enough
"""

import math


def stack_height_3d(layers):
    if layers <= 0:
        return 0.0

    # Altura total = diâmetro da primeira camada + (layers-1) * espaçamento vertical
    # Espaçamento vertical = diâmetro / √2
    spacing = 1.0 / math.sqrt(2.0)
    height = 1.0 + (layers - 1) * spacing

    return height

# Teste

print(stack_height_3d(0))
print(stack_height_3d(1))
print(stack_height_3d(2))
