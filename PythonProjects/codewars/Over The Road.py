# You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:
# 1|   |6
# 3|   |4
# 5|   |2

# Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.

# Given your house number address and length of street n, give the house number on the opposite side of the street.

# My_Code
# def over_the_road(address, n):
#     address = 1
#     total_house = n*2
#     if n == 3:
#         while n < total_house:
#             if address % 2 == 0:
#                 print(str(total_house)+'|', '|'+str(address)+'\n', sep='\t')
#                 total_house = total_house-1
#                 address = address+1
#             else:
#                 print(str(address)+'|', '|'+str(total_house)+'\n', sep='\t')
#                 total_house = total_house-1
#                 address = address+1
#     else:
#         while n < total_house:
#             if address % 2 == 0:
#                 print(str(total_house)+'|', '|'+str(address)+'\n', sep='\t')
#                 total_house = total_house-1
#                 address = address+1
#             else:
#                 print(str(address)+'|', '|'+str(total_house)+'\n', sep='\t')
#                 total_house = total_house-1
#                 address = address+1


# Test 1
# over_the_road(1, 3)
# Neighbour = 6

# Test 2
# over_the_road(2, 3)
# Neighbour = 5

# Test 3
# over_the_road(3, 3)
# Neighbour = 4

# Test 4
# over_the_road(3, 5)
# Neighbour = 8

# Test 5
# over_the_road(7, 11)
# Neighbour = 16


# Solution
def over_the_road(address, n):
    return (2*n + 1 - address)


print(over_the_road(3, 5))
