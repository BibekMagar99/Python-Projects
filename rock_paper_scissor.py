import random
def game():
    while True:
        cpu = random.choice(['r', 'p', 's'])
        print("\n\n\n\n\nplease enter : 'r' for rock,   'p' for paper and      's' for scissor :")
        you = input("enter here :  ").lower()
        if you in ['r','p','s']:
        #nice one... yo can compare the input in this list
        
            if (you =='r' and cpu =='s'):
                print(f"cpu : {cpu}\nyou : {you}\nrock beats scissor....!\n You win!")
            elif (you =='s' and cpu =='p'):
                print(f"cpu : {cpu}\nyou : {you}\nsciccor beats paper....!\n You win!")

            elif (you == cpu):
                print(f"cpu : {cpu}\nyou : {you}\nIt's a tie!")
            else:
                print(f"cpu : {cpu}\nyou : {you}\nyou've lost! Try again")
            break
        else:
            print("\n\n\n\nplease enter valid character")

print("do you want to play rock,paper,scissor ??")
answer = input("please type 'y' for yes and 'n' for no :  ").lower()
if answer == "y":
        while True:
            game()
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
    
