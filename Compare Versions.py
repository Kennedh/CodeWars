"""
Karan's company makes software that provides different features based on the version of operating system of the user.

To compare versions, Karan currently parses both version numbers as floats.

While this worked for OS versions 10.6, 10.7, 10.8 and 10.9, the operating system company just released OS
version 10.10. This causes his method to fail, as 10.9 is greater than 10.10 when interpreting both as numbers,
despite being a lesser version.

Help Karan by writing him a function which compares two versions, and returns whether or not the first one is greater
than or equal to the second.

Specification notes:

Versions are provided as strings of one or more integers separated by ..
The version strings will never be empty.
The two versions are not guaranteed to have an equal amount of sub-versions, when this happens assume that all
missing sub-versions are zero.
Two versions which differ only by trailing zero sub-versions will never be given.

"""

def compare_versions(version1, version2):
    v1_parts = [int(x) for x in version1.split('.')]
    v2_parts = [int(x) for x in version2.split('.')]
    max_length = max(len(v1_parts), len(v2_parts))
    v1_parts.extend([0] * (max_length - len(v1_parts)))
    v2_parts.extend([0] * (max_length - len(v2_parts)))
    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 > v2:
            return True
        elif v1 < v2:
            return False
    return True

# Teste

print(compare_versions("10.6", "10.10"))  # False (10.6 < 10.10)
print(compare_versions("10.10", "10.6"))  # True (10.10 > 10.6)
print(compare_versions("10.9", "10.10"))  # False (10.9 < 10.10)
print(compare_versions("10.10", "10.9"))  # True (10.10 > 10.9)
print(compare_versions("1.0", "1.0.0"))   # True (são iguais)
print(compare_versions("2.0", "1.9.9"))   # True (2.0 > 1.9.9)
print(compare_versions("1.0.1", "1.0.2")) # False (1.0.1 < 1.0.2)