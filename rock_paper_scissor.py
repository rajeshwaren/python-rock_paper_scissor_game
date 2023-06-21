import random
options=["rock","paper","scissors"]
user_point=0
computer_point=0
print("     WELCOME TO THE GAME    ")
next_round=""
while(next_round==""):
    #-----computers-----------------
    computer_choice=random.choice(options)
    #----------------------------------


    #--------user----------------------
    user_input=input("Pick your option \n1.rock \n2.paper \n3.scissors \nEner (1/2/3)  :")
    
    entry_check_1=["1","2","3"]
    if user_input in entry_check_1:
        user_input=int(user_input)
        user_choice=options[user_input-1]
    #-------------------------------------



    #--------Report------------------------
        print("You picked",user_choice)
        print("Computer picked",computer_choice)


        if computer_choice=="paper" and user_choice=="scissors":
            print("you won this match")
            user_point+=1
        elif computer_choice=="rock" and user_choice=="paper":
            print("you won this match")
            user_point+=1
        elif computer_choice=="scissors" and user_choice=="rock":
            print("you won this match")
            user_point+=1
        elif computer_choice==user_choice:
            print("match draw")
        else:
            print("Computer won this match")
            computer_point+=1

        print("your total score",user_point)
        print("computer's total score",computer_point)
        next_round=input("Enter q to quit \nTo continue press Enter key....")
        if next_round =="q":
            break
    else:
        print("check your input!!!")

