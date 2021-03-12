import random
#to initialize the pseudo random generator
import time
#delay halna ko lagi


def computer_guess():
    low = 1
    high = 100
    feedback = ""
    while feedback != "c" :
        ''' yo if else chai chaincha.... because if hamro guess chai 5 ho re, ani computer
    guessed 6 then high vancham and tesle -1 garera high ma rakhcha, i.e high =5
    again if 4 guess garyo vani we will say low so
    4+1 garera halcha low=5
    now random.randint le (5,5)paucha so error nikalcha....nikalnu parne ho tara eta nikalena,.. so let it be i error nikalyo vani chai)'''

        '''
        if high!=low :
            guess = random.randint(low,high)
        else :
            guess = low #high rakhe ni milcha'''

        guess = random.randint(low,high)
        print(f"Is it.... {guess}\nplease Specify whether it is hig or low")
        print("please input the following\n'h' for high\n'l' for low")
        feedback = input("Input :  ").lower()
        if feedback == 'h' :
            high = guess-1
        elif feedback == 'l' :
            low = guess+1
        else :
            print("please enter valid character !")
    print("I've guessed it correct!")
    time.sleep(2)
    print("Now you shall become my slave.....Filthy Human!")
    time.sleep(1)
    print("\n\nHa...Ha....Haaaaaa!!!\n\n\n\n\n\n\n\n\n")
    time.sleep(5)
    print("just kiddin!")

print("do you want to play a game ??")
answer = input("please type 'y' for yes and 'n' for no :  ").lower()
if answer == "y":
        
        while True:
            print("\n\n\n\n\nThanks, I have been feeling lonely lately...")
            time.sleep(1)
            print("Glad that you're playing with me!")
            time.sleep(1)
            print("\n\n\n\nThink about a number between 1 to 100\n\n\n\n\n")
            time.sleep(5)
            print("Now, I'll guess the number")
            time.sleep(3)
            print("Ok! let me guess..............!")
            time.sleep(2)
            computer_guess()
            again = input("Do you want to play again? (Y/N)\nAnswer :").lower()
            if again == 'y':
                continue    
            elif again == 'n' :
                print("thanks for playing !")
                break
            else :
                print("please input valid character")
        
elif answer == "n":
    print("Thankyou !") 
else:
    print("please input a valid character")

     
