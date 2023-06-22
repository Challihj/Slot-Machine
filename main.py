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
        if amount.isdigit(): #check if wager amount is a valid number (not negative)
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Wager must be greater than 0")
        else:
            print("Please enter a valid wager")
    
    return amount

def get_lines():
    while True:
        lines = input("Enter number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #check if lines entered is a valid number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: # check if lines entered is valid (between 1 and 3)
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number between 1 and " + str(MAX_LINES))
    
    return lines

def get_bet():
    while True:
        amount = input("Bet amount on each line: $")
        if amount.isdigit(): #check if amount is a digit
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid bet")
    
    return amount

def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet  = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. Current balance: ${balance}, amount attempted: ${total_bet}")        
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    slot_output(slots)

main()

