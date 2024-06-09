# 1 Writing name to file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# 2 Reading name from file
with open("name.txt", 'r') as file:
    name = file.read().strip()
print(f"Hi {name}!")

# 3 Reading and adding first two numbers from file
with open("numbers.txt", 'r') as file:
    numbers = file.readlines()
result = int(numbers[0]) + int(numbers[1])
print(result)

# 4 Printing total for all lines in file
with open("numbers.txt", 'r') as file:
    total = sum(int(line) for line in file)
print(total)
