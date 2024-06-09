import random

def main():
    user_score = int(input("Enter your score: "))
    print_result(user_score)
    random_score = random.randint(0, 100)
    print("Random Score:", random_score)
    print_result(random_score)


def print_result(score):
    result = determine_result(score)
    print(f"Score {score} is {result}")


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()
