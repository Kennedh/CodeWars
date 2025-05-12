"""
Dados alguns pontos (coordenadas cartesianas), retorne verdadeiro se todos eles estiverem em uma reta.
Trate tanto um conjunto vazio quanto um único ponto como uma reta.

on_line(((1,2), (7,4), (22,9)) == True
on_line(((1,2), (-3,-14), (22,9))) == False
"""


def on_line(points):
    if len(points) <= 2:
        return True

    x0, y0 = points[0]
    base_found = False
    for i in range(1, len(points)):
        x1, y1 = points[i]
        if (x1, y1) != (x0, y0):
            base_found = True
            break

    if not base_found:
        return True

    for x, y in points:
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
            return False
    return True

# Teste

print(on_line(((1,2), (7,4), (22,9))))
