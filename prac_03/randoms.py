import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


#1.This function returns a random integer between the specified range (inclusive of both endpoints).
#  Smallest possible number: 5, Largest possible number: 20
#2.This function returns a randomly selected element from the range created by range(3, 10, 2).
#   Smallest possible number: 3, Largest possible number: 9
#  No, line 2 could not have produced a 4.
#3.This returns a float and includes both endpoints in the range.
#  Smallest possible number: 2.5, Largest possible number: 5.5

random_number = random.randint(1, 100)
print(random_number)