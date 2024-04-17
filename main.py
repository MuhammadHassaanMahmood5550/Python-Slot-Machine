import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_And_COUNT = {
   "A": 2,
   "B": 4,
   "C": 6,
   "D": 8    
}

WINNING_SYMBOL_POINTS = {
   "A": 5,
   "B": 4,
   "C": 3,
   "D": 2  
}

def get_slot_machine_spin(rows, cols, symbols):
    # first we need to add two "A"s, 4 "B"s, 6 "C"s and 8 "D"s in a list
    all_syombols_list = []
    for its_key, element in SYMBOL_And_COUNT.items():
        for _ in range(element): # notice we do not need i variable so we write _ means don't declear
            all_syombols_list.append(its_key)
    
    print("so far we have", all_syombols_list)

    # now we need to randomly select each element in all_syombols_list for our column
    columns = []
    symbols_copy = all_syombols_list[:]
    for i in range(cols):
        temp_column = []
        for j in range(rows):
            radom_symbol = random.choice(symbols_copy)
            symbols_copy.remove(radom_symbol)
            temp_column.append(radom_symbol)
        
        columns.append(temp_column)

    print("random value columns", columns)        
    return columns

# print columns lins in a order/format
def print_slot_machine(columns):
    for i in range(len(columns[0])):
        for j, element in enumerate(columns):
            if j != len(columns[0]) - 1:
                print(element[i], end=" | ")
            else:
                print(element[i])               

 # check if lines same
def check_wining(colums, lines, bet ,values):
#    winning_list = []
     winnings = 0
     winning_lines = []
#    for i, element in enumerate(colums):
     for i in range(lines):
       symbol = colums[i][i]
    #    print("i=-", i, " colums[i][0] ", colums[i][i], " symbol ", symbol)
       # is_true = True
       for j in colums:
        #    print("j=-", j[i])
           if j[i] != symbol:
               break
            # is_true = False
            # if is_true:
       else:
        #    print("winner is", j[i])
    #        #    winning_list.append({symbol: WINNING_SYMBOL_POINTS[symbol]})
           winnings = winnings + WINNING_SYMBOL_POINTS[symbol] * bet
           winning_lines.append(i + 1)

    #  print("winnings", winnings, "winning_lines", winning_lines) 
     return winnings, winning_lines     

        
      







def deposite():
    while True:
        amount = input("What amount you would like to deposite $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("amount okay")
                break
            else:
                print("Amount must be grater than 0")    
        else:
            print("Please Enter a valid number")

    return amount

def enter_number_of_lines():
    while True:
        lines = input("Please enter no of line to bet on (1 - " + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                print("lines okay")
                break
            else:
                print("please enter valid number of lines")
        else:
            print("please enter a valid number")

    return lines       

def enter_bet():
    while True:
        bet = input("what would you like to bet on each line $")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                print("bet okay")
                break
            else:
                print(f"bet amount should be between {MIN_BET} - {MAX_BET}")
        else:
            print("please enter a valid number")   
    return bet    

def spin(balance):
       lines = enter_number_of_lines()
       while True:  
          bet = enter_bet()
          total_bet = lines * bet
          if total_bet <= balance:
               break
          else:
              print(f"You balance is insufficiant, your current balance is ${balance}")
           
       
       columns = get_slot_machine_spin(ROWS, COLS, SYMBOL_And_COUNT)
       print_slot_machine(columns)
       # check_wining(colums, lines, bet ,values):
       wins, on_lines = check_wining(columns, lines, bet, 10)
       print(f"you won ${wins} on lines ", *on_lines) 
       if wins > 0: 
           balance += wins 
       else: 
           balance -= bet

       print("balance on fun", balance)
       return balance    


def main_func():
   balance = deposite()
   while True:
       if balance > 0:
          balance = spin(balance)
          print("balance now", balance) 
       else:
           print(f"you are out of balance = ${balance}") 
           print("would you like to play again ? yes|no ")
           check = input("would you like to play again, yes|no ? ")
           if check == "yes":
               balance = deposite()
           else: 
               break 

main_func()