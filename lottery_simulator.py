import random

def simulate_lottery():
    # Draw 5 unique numbers between 1 and 70
    winning_numbers = random.sample(range(1, 71), 5)
    winning_numbers.sort()

    # Draw the Super Ball between 1 and 30
    super_ball = random.randint(1, 30)

    return winning_numbers, super_ball

def get_user_numbers():
    print("Enter 5 unique numbers between 1 and 70:")
    user_numbers = []
    while len(user_numbers) < 5:
        try:
            num = int(input(f"Number {len(user_numbers)+1}: "))
            if num < 1 or num > 70:
                print("Number must be between 1 and 70.")
            elif num in user_numbers:
                print("Number already chosen. Please select a unique number.")
            else:
                user_numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    user_numbers.sort()

    while True:
        try:
            super_ball = int(input("Enter your Super Ball number (1-30): "))
            if 1 <= super_ball <= 30:
                break
            else:
                print("Super Ball number must be between 1 and 30.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return user_numbers, super_ball

def determine_prize(matches, super_ball_match):
    if matches == 5 and super_ball_match:
        return "Jackpot!"
    elif matches == 5:
        return "$1,000,000"
    elif matches == 4 and super_ball_match:
        return "$10,000"
    elif matches == 4:
        return "$500"
    elif matches == 3 and super_ball_match:
        return "$200"
    elif matches == 3:
        return "$10"
    elif matches == 2 and super_ball_match:
        return "$10"
    elif matches == 1 and super_ball_match:
        return "$4"
    elif super_ball_match:
        return "$2"
    else:
        return "No Prize"

def main():
    print("Welcome to the Lottery Simulator!")
    user_numbers, user_super_ball = get_user_numbers()
    winning_numbers, winning_super_ball = simulate_lottery()

    print("\nYour Numbers:", user_numbers)
    print("Your Super Ball:", user_super_ball)
    print("\nWinning Numbers:", winning_numbers)
    print("Winning Super Ball:", winning_super_ball)

    matches = len(set(user_numbers) & set(winning_numbers))
    super_ball_match = user_super_ball == winning_super_ball

    print(f"\nYou matched {matches} numbers.")
    if super_ball_match:
        print("You matched the Super Ball!")
    else:
        print("You did not match the Super Ball.")

    prize = determine_prize(matches, super_ball_match)
    print(f"Your prize: {prize}")

if __name__ == "__main__":
    main()