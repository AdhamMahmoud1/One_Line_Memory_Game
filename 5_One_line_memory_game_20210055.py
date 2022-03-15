import random
my_list = ["A","B","C","D","E","F","G","H","I","J","A","B","C","D","E","F","G","H","I","J"]
num     = ["1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0"]
random.shuffle(my_list)
score_player1 = 0   
def player1():
    global score_player1 
    print("Player1 is Turn.") 
    print("Welcome: ")
    print(" ".join(num))
    a = int(input())
    b = int(input())
    print(f"Player#1_score {score_player1}: {a},{b} ")
    print(my_list[a-1], my_list[b-1])
    if a == b:
        print("Invalid input 'You can't enter two equaled numbers!'")
    elif my_list[a-1] == my_list[b-1]:
        num[a-1] = "*" ; num[b-1] = "*"
        print(" ".join(num))
        score_player1 += 1
        print(f"Player1 is  score: {score_player1}")
        print("Screen is cleared.")
    else:
        print("Wrong!!")
        print("screen is cleared.")
score_player2 = 0
def player2():
    global score_player2 
    print("Player2 is Turn.")
    print("Welcome: ")
    print(" ".join(num))
    a = int(input())
    b = int(input())
    print(f"Player#2_score {score_player2}: {a},{b} ")
    print(my_list[a-1], my_list[b-1])
    if a == b:
        print("Invalid input 'You can't enter two equaled numbers!'")
    elif my_list[a-1] == my_list[b-1]:
        num[a-1] = "*" ; num[b-1] = "*"
        print(" ".join(num))
        score_player2 += 1
        print(f"Player2 is  score: {score_player2}")
        print("Screen is cleared.")
    else:
        print("Wrong!!")
        print("screen is cleared.")
        
print(f"Hllo in One line memory game\n", " ".join(my_list))
print("Player 1 starts the game.")
while True :
    player1()
    player2()
    if score_player1 + score_player2 == 10:
        if score_player1 == score_player2:
            print("The game is ended by Draw!!!")
        elif score_player1 > score_player2:    
            print("Congratulation!\nPlayer 1 is the Winner!!!")
        else:   
            print("Congratulation!\nPlayer 2 is the Winner!!!")
        break    
print("End of the game!!!")  

    

