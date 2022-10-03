#Global constant
MAX_LINES = 3 
MAX_BET= 200
MIN_BET = 50



from curses.ascii import isdigit

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
 bet = get_bet()
 total_bet = bet * lines

 print(f"You are betting ${bet} on {lines} lines. Total bet amount is : ${total_bet}")

 print(balance, lines)

main()

