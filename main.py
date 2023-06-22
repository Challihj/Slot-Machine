import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Dimensions of slot machine
ROWS = 3
COLS = 3

# Symbols in each column (slot machine reel)
symbol_count = {
    "♠": 2, 
    "♥": 4,
    "♦": 6,
    "♣": 8 
}
# Assigning value to each symbol
symbol_value = {
    "♠": 5, 
    "♥": 4,
    "♦": 3,
    "♣": 2 
}
def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
       for _ in range(symbol_count):
           all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def slot_output(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("Wager amount: $")
        if amount.isdigit(): # Check if wager amount is a valid number (not negative)
            amount = int(amount)
            if amount > 0: # Check that wager amount is more than 0
                break
            else:
                print("Wager must be greater than 0")
        else:
            print("Please enter a valid wager")
    
    return amount

def get_lines():
    while True:
        lines = input("Enter number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # Check if lines entered is a valid number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: # Check if lines entered is valid (between 1 and 3)
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number between 1 and " + str(MAX_LINES))
    
    return lines

def get_bet():
    while True:
        amount = input("Bet amount on each line: $")
        if amount.isdigit(): # Check if amount is a digit
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: # Check that bet is between min and max allowed
                break
            else: # When bet is not between min and max
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid bet") # Prints when bet is not a valid number
    
    return amount

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet  = bet * lines

        if total_bet > balance: # Checks if total bet is more than players balance
            print(f"Insufficient funds. Current balance: ${balance}, amount attempted: ${total_bet}")        
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    slot_output(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    
    if winnings == 0:
        print("Sorry, you did not win")
    else:
        print(f"Winner Winner Chicken Dinner \nYou won: ${winnings}!")
        print(f"You won on line(s): ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        if balance == 0:
            print("Out of money :( Thank you for playing!")
            break
        else:
            answer = input("Press enter to play (q to quit)")
            if answer == "q":
                break
        
        balance += spin(balance)
        
    print(f"You cashed out with an final balance of: ${balance}")
    

main()

