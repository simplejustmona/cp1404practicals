def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

def get_numbers():
    user_input = input("Enter numbers separated by commas: ")
    try:
        numbers = [float(num) for num in user_input.split(",")]
        return numbers
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return []

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def display_numbers(numbers):
    numbers.sort()
    print("..".join(map(str, numbers)))

def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

if __name__ == "__main__":
    main()
