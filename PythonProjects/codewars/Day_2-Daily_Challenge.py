# Challenge_1

squares = [1, 4, 9, 16, 25]
# print(squares[-3]:)
# What is the output of this code?

# My_Solution
# What is the output of this code?
# My_Answer=9

# Checks
print('Challenge_1')
print(squares[-3:], '\n')

# Explanation
# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. Like strings (and all other built-in sequence type), lists can be indexed and sliced.

# Challenge_2


def srange(x):
    return range(x-3, x)


s = 0
for i in srange(2):
    s += i

print('Challenge_2')
print(s, '\n')

# What is the output of this code?
# My_Answer=[1,2,3,4]

# Checks
# Answer=0
# Explanation
# In the puzzle we define our own range function srange(x).
# It creates a range object using the built-in range() function.
# Calling range(start, stop) returns a range object with range-values from start to stop-1.
# Therefore srange(x) returns a range from x-3 to x-1.
# When we call the function srange() with x=2 it returns a range object with the values -1, 0, 1.
# In the loop we sum up these values and get the output 0.


# Challenge_3

x = 50//11

print('Challenge_3')
print(x, '\n')

# What is the output of this code?
# My_Answer=4

# Checks
# Answer=4

# Explanation
# When I started to learn Python 3, I used to be confused about the semantics of dividing two integers. Is the result a float or an integer value? The reason for my confusion was a nasty Java bug that I once found in my code. The code was supposed to perform a simple division of two integers and return a float parameter value between zero and one. But Java uses integer division, i.e., it skips the remainder. Thus, the value was always either zero or one, but took never a value in-between. It took me days to figure that out.

# Save yourself the debugging time by memorizing the following rule once and for all.

# The // operator performs integer (floor) division and the / operator performs float (true) division. An example for floor division is 50 // 11 = 4. An example for true division is 50 / 11 = 4.545454545454546.

# Note that floor division always rounds ''down'', i.e., 3 // 2 == 1 and -3 // 2 == -2.

# Although the puzzle seems simple, more than twenty percent of the Finxter users cannot solve it.


# Challenge_4

# SequencePuzzle
seq = [30, 9, 40, 50, 91, 142, 234]

print('Challenge_4\n')

seq[i] = seq[i-2] + seq[i-1] + 1
# What's the next element in the list?
# My_Answer=377

# Challenge_5
prefix = 'Fi'
print('Challenge_5')
print(prefix+'nxter')

#  What is the output of this code?
# My_Answer=Finxter

# Checks
# Answer=Finxter
