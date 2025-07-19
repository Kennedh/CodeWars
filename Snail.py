"""
Dado um n x n array, retorne os elementos do array organizados dos elementos mais externos para o elemento do meio,
no sentido horário.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
Para melhor compreensão, siga os números da próxima matriz consecutivamente:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

def snail(snail_map):
    if not snail_map or not snail_map[0]:
        return []
    else:
        n = len(snail_map)
        top = 0
        bot = n -1
        left = 0
        right = n -1
        res = []
        while top <= bot and left <= right:

            for j in range(left, right + 1):
                res.append(snail_map[top][j])
            top += 1

            for i in range(top, bot + 1):
                res.append(snail_map[i][right])
            right -= 1

            if top <= bot:
                for j in range(right, left - 1, -1):
                    res.append(snail_map[bot][j])
                bot -= 1

            if left <= right:
                for i in range(bot, top - 1, -1):
                    res.append(snail_map[i][left])
                left += 1

        return res


# Teste

print(snail([[1,2,3],
             [4,5,6],
             [7,8,9]]))
