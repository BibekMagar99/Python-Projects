import random
def game():
    print("This is a simple game, Just guess the number between the range 1 to 20 !")
    guess = 0
    random_number = random.randint(1,20)    
    while guess!= random_number :
        guess = int(input("please enter your guessed integer :  "))
        try:
            if guess > random_number :
                print("mathi vo")
            else :
                print("tala vo")
        except ValueError:
            try:
                val = float(user_input)
                print("Input is a float  number.\nplease enter valid integer")
            except ValueError:
                print("No.. input is not a number. It's a string\nPlease enter valid integer")
    print("\n\n\nNice !!!!")



print("do you want to play guess the number with me ??")
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

     

     
