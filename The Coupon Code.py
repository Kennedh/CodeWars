"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
"""

from datetime import datetime

from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if type(entered_code) is not type(correct_code):
        return False
    if entered_code != correct_code:
        return False
    date_format = "%B %d, %Y"
    try:
        d1 = datetime.strptime(current_date, date_format)
        d2 = datetime.strptime(expiration_date, date_format)
        return d1 <= d2
    except:
        return False


# Test cases

print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))  # True
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))  # False
print(check_coupon("123", "456", "July 9, 2015", "July 9, 2015"))  # False
print(check_coupon("ABC", "ABC", "December 31, 2023", "January 1, 2024"))  # True
print(check_coupon("ABC", "ABC", "January 2, 2024", "January 1, 2024"))  # False