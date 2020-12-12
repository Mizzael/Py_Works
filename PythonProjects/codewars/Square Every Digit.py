# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns an integer

# My Code
def square_digits(num):
    square = ''
    for temp in str(num):
        square += str(int(temp)**2)
    return int(square)


print(square_digits(9119))

# (list(map(int, str(num))))
