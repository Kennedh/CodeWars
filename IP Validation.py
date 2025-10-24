"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
"""

def is_valid_IP(strng):
    if strng == "":
        return False
    temp = strng.split(".")
    if len(temp) != 4:
        return False
    for n in temp:
        if not n.isdigit():
            return False
        if str(int(n)) != n or int(n) > 255:
            return False
    return True

# Teste

print(is_valid_IP('123.045.067.089'))
print(is_valid_IP('127.1.1.0'))
print(is_valid_IP('0.0.0.0'))
print(is_valid_IP('0.34.82.53'))
print(is_valid_IP('192.168.1.300'))