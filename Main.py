import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}


def check_winnings(columns, lines, bet, values):
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
            winning_lines.append(lines)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbols)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns  
 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(column) - 1:
                print(column[row],  end = " | ")
            else:
                print(column[row])
        print()

def deposit():
    while True:
        amount = input("Enter a Valid Amount you would like to deoposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print("Enter a Value greater than 0")
        else:
            print("Please enter a number")
    return amount

def No_of_Lines():
    while True:
        lines = input("Enter a Valid No of lines (1 - " + str(MAX_LINES) +") ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a line between 1 and "+ str(MAX_LINES))
        else:
            print("Enter a number")
    return lines

def Bet_Value():
    while True:
        amount = input("Enter a betting amount on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter the amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a number")
    return amount


def spin(amount):
    lines = No_of_Lines()
    while True:
        bet = Bet_Value()
        total_bet = lines * bet
        if total_bet > amount:
            print(f"You don't have enough money to make that deposit, your currency balance is ${amount}")
            quit = input("Do you want to quit?")
            if quit == "q":
                break
        else:
            break
    print(f"The bet is placed on line {lines} and the amount is ${bet}. The total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    print(f"you won ${winnings}")
    print(f"You won on: ", *winning_lines)

    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        ans = input("Press Enter to Play the Game Else press Q to quit")
        if ans == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()