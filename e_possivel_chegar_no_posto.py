def zero_fuel(distance_to_pump, mpg, fuel_left):
    poss_distance = mpg * fuel_left
    return poss_distance >= distance_to_pump