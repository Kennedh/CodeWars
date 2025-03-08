def square_digits(num):
    result = ""
    for i in str(num):
        result += str(int(i) * int(i))
    return int(result)

# Teste

print(square_digits(9119))


