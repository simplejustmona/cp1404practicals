"""
names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
while True:
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f"{name_to_remove} has been removed")

    else:
        print(f"{name_to_remove} does not exist")
        break
    print(f"updated list: " + ", ".join(names))
"""
"""
#toStudy
things = [True, 1.2, "Good", [1, 10]]
print(things [-2])
print("%" . join([things[2][1:-1]]))
print([str(t)[0] for t in things])
print([len(str(t)) for t in things])
print([t for t in things if type(t) in (float, int)]) #Trueisanin
print([t for t in things if isinstance(t, int)]) #True
"""
values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values [0][0]
for row in range(0, len(values)) : #2
    for column in range(0, len(values[row])): #4
        if v < values[row][column]:
            v = values[row] [column]
print(v)
#numbers
#people
#ages
#index
"""with open("numbers.txt", "r") as input_file: #datas will be strings after reading from file
    numbers = input_file. readlines() #this will turn numbers to least
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += float (number)
    print(f"Total sum of numbers is {sum_of_numbers}")

with open("numbers.txt", "r") as file:
    for line in file:
        try:
            num = int(line.strip())  # Convert to integer
            sum_of_numbers += num
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")
print(f"Total sum of integers: {sum_of_numbers}")
"""
with open("numbers.txt", "r")as input_file:
    for number in input_file:
        sum_of_numbers= float (number )
print(f"total sum of numbers is{sum_of_numbers}