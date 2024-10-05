import random  # Importing the random module to randomly select symbols

# Function to simulate spinning a row of symbols in the slot machine
def spin_row():
    # List of possible symbols that can appear on the slot machine
    symbol = ['🍉', '🍊', '🍋', '🍑', '🐬']

    # Return a list of three randomly chosen symbols
    return [random.choice(symbol) for _ in range(3)]

# Function to print a row of symbols in a formatted way
def print_row(row):
    print("------")
    # Joining the symbols with " | " to represent the slot machine row
    print(" | ".join(row))
    print("------")

# Function to calculate the payout based on the row of symbols and the player's bet
def get_payout(row, bet):
    # Check if all three symbols in the row are the same
    if row[0] == row[1] == row[2]:
        # Determine payout based on which symbol appears
        if row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍊':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🍑':
            return bet * 10
        elif row[0] == '🐬':
            return bet * 20
    # Return 0 if no match
    return 0

# Main function to run the slot machine game
def main():
    # Initial balance for the player
    balance = 200

    # Welcome message and display the symbols
    print("=============================")
    print("Welcome to Hakari's casino")
    print("Symbols: 🍉 | 🍊 | 🍋 | 🍑 | 🐬")
    print("Always bet on Hakari")
    print("=============================")

    # Game loop, continues as long as the player has a positive balance
    while balance > 0:
        # Display current balance
        print(f"Current balance: ${balance}")

        # Ask the player for their bet
        bet = input("Place your bet amount: ")

        # Validate if the input is a number
        if not bet.isdigit():
            print("Invalid amount")
            continue

        bet = int(bet)  # Convert the valid bet input to an integer

        # Check if the player has enough balance for the bet
        if bet > balance:
            print("Bro ur broke do it again")
            continue
        # Ensure the bet is greater than 0
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        # Deduct the bet amount from the player's balance
        balance -= bet

        # Spin the slot machine (randomly generate a row of symbols)
        row = spin_row()
        print("Spinning...\n")
        # Print the row of symbols
        print_row(row)

        # Calculate the payout based on the result of the spin
        payout = get_payout(row, bet)

        # If the player wins, show the payout
        if payout > 0:
            print(f"Nice you won ${payout}")
        # If no payout, print a message encouraging to bet on Hakari
        elif payout == 0:
            print("I said always bet on Hakari")

        # Add the payout to the player's balance
        balance += payout

# Entry point of the program, only runs when the script is executed directly
if __name__ == '__main__':
    main()
