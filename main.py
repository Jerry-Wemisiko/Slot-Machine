import random #generate random values for slot machines

from curses.ascii import isdigit





#Global constants
MAX_LINES = 3 
MAX_BET= 200
MIN_BET = 50

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
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





# func to receive depossit for bets
def deposit():
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount> 0:
                break
            else:
                print("Amount must be greater than 0")

        else:
            print("Please enter an amount")

    return amount


# function to det number of nlines one wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on 1-" + str(MAX_LINES) + ")?")

        if lines.isdigit():
            lines = int(lines)

            #ststement to check if a value is btn two values
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")

        else:
            print("Please enter a number ")

    return lines

#func for bet amount
def get_bet():
     while True:
        amount = input("Enter a bet amount? $ ")

        if amount.isdigit():
            amount = int(amount)

            #ststement to check if a value is btn two values - BET amount
            #  IS BTN THE MIN AND MAX
            if MIN_BET <= amount<= MAX_BET:
                break
            else:
                #f string to add variables in a string
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

        else:
            print("Please enter a number ")

     return amount

def main():
 balance = deposit()
 lines = get_number_of_lines()

 #checking if amount is within the deposit
 while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance :
        print(
            f"You do not have enough amount to place bet, your balance is: ${balance} ")

    else:
        break

 print( 
    f"You are betting ${bet} on {lines} lines. Total bet amount is : ${total_bet}")

 print(balance, lines)

main()

