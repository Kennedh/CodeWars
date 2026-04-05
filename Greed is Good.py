"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw
according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
(contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
Note: your solution must not modify the input list.
"""

def score(dice):
    counts = {}
    points = {2: 200, 3: 300, 4: 400, 6: 600}
    total = 0
    for num in range(1,7):
        if num in dice:
            counts[num] = dice.count(num)
    for key in counts.keys():
        if key in (2,3,4,6) and counts[key] >= 3:
            total += points[key]
        if key == 1:
            if counts[key] >= 3:
                total += 1000 + ((counts[key] % 3) * 100)
            else:
                total += 100 * counts[key]
        if key == 5:
            if counts[key] >= 3:
                total += 500 + ((counts[key] % 3) * 50)
            else:
                total += 50 * counts[key]
    return total



# Teste

print(score([5,1,3,4,1]))
print(score([1,1,1,3,1]))
print(score([2,4,4,5,4]))



