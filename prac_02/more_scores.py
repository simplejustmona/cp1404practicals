import random

def print_results(scores):
    with open("results.txt", "w") as file:
        for score in scores:
            result = determine_result(score)
            file.write(f"{score} is {result}\n")

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"

def main():
    num_scores = int(input("Enter the number of scores: "))
    scores = [random.randint(0, 100) for _ in range(num_scores)]
    print_results(scores)

if __name__ == "__main__":
    main()
