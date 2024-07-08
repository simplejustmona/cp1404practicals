def get_numbers(numbers):
    get_num = input("Enter numbers separated by commas: ")
    numbers = [float(num) for num in get_num.split(",")]

def calculation(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def display(numbers):
    print("..".join(numbers))

def main():
    numbers = get_numbers
    calculation(numbers)
    display(numbers)

if __name__ == "__main__":
    main()