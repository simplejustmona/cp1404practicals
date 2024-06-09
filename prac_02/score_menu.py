import random


def main():
    valid_scores = []
    score = get_valid_score()
    valid_scores.append(score)

    while True:
        print_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
            valid_scores.append(score)
        elif choice == "P":
            print_result(valid_scores[-1])
        elif choice == "S":
            show_stars(valid_scores[-1])
        elif choice == "Q":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_result(score):
    pass


def show_stars(score):
    stars = "*" * score
    print(stars)


def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


if __name__ == "__main__":
    main()
