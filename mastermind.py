import random


def get_guess():
    listy = []
    
    while len(listy) < 4:
        q = int(input(" Guess a number: "))
        if q < 1 or q > 7:
            print("You can only use numbers 1-7 as guesses!")
        elif q >= 1 and q <= 7:
            if q not in listy:
                listy.append(q)
            else: 
                print("You can only use each number once!")
        
    print(listy)
    return listy



def check_values(cl,ul):
    listy = []
    for i in range(4):
        if ul[i] in cl and ul[i] != cl[i]:
            listy.append("WHITE")
        elif ul[i] == cl [i]:
            listy.append("RED")
        else: 
            listy.append("BLACK")
    random.shuffle(listy)
    print(listy)
    check_win(listy)
    return listy



def check_win(response_list):
    if response_list[0] == "RED" and response_list[1] == "RED" and response_list[2] == "RED" and response_list[3] == "RED":
        print("You win!!!")
        return "You win"
        
    else:
        return "keep trying"
    
        



def create_comp_list():
    listy = []

    while len(listy) < 4:
        ran = random.randint(1,7)
        
        if ran not in listy:
            listy.append(ran)
    
    
    
    return listy




def play_game():
    print('''Instruction: You have 5 guesses
    If a number in the your guessed list is in the computer list, but not in the correct index, the response should be 'WHITE'.
If a number in the your guessed list is in the computer list and in the same index, the response should be 'RED'
If the number in the your guessed list is not in the computer list, the response should be 'BLACK'.''')
    cl = create_comp_list()
    guesses = 5
    while guesses != 0:
        inp = check_values(cl,get_guess())
        win = check_win(inp)
        if win == "You win":
            break
        guesses -= 1
        print(f"you have {guesses} guesses left" )
        
        




# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.



play_game()
