def game():
    print("You've entered the learning zone.......\nplease put the correct answers to get the medal")
    answer_1 = input("1. Is indentation important ?(Y/N)\nAnswer : ").lower()
    if answer_1 == "y" :
        print("you got that correct ! ...... attaboy!\n\n\n")
        answer_2 = input("2. What is the least amount of space required for indentation ?\nAnswer :").lower()
        if answer_2 == "1" :
            print("Nice !\n\n\n")
            answer_3 = input("3. x, y = 10, 20\nx, y = y, x\nprint(x, y)\n\n\nWhat is the Output of this program ?\na) 10,20\nb) 20,10\nAnswer :").lower()
            if answer_3 == "b" :
                print("You're almost there !\n\n\n")
                answer_4 = input("4. a = \"GeeksForGeeks\"\nprint(\"Reverse is\", a[::-1])\n\n\nWhat is the Output of this program ?\na) ks\nb) skeeGroFskeeG\nAnswer :").lower()
                if answer_4 == "b" :
                    print("Last One!\n\n\n")
                    answer_5 = input("test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]\nHow do you print the max repeated number ?\na) print(max(set(test), key = test.count))\nb)print(max(key = test.count))\nAnswer : ").lower()
                    if answer_5 == "a" :
                        print("                          Congratulations !     ")
                        print("                          _______________       ")
                        print("                          |@@@@|     |####|     ")
                        print("                          |@@@@|     |####|             ")
                        print("                          |@@@@|     |####|           ")
                        print("                          \@@@@|     |####/               ")
                        print("                           \@@@|     |###/            ")
                        print("                            `@@|_____|##'             ")
                        print("                                 (O)                 ")
                        print("                              .-'''''-.               ")
                        print("                            .'  * * *  `.               ")
                        print("                           :  *       *  :              ")
                        print("                          : ~    N O.   ~ :           ")
                        print("                          : ~   O N E   ~ :            ")
                        print("                           :  *       *  :              ")
                        print("                            `.  * * *  .'                ")
                        print("                              `-.....-'                ")
                    else :
                        enter1= input("please Try again")
                else :
                    enter1= input("please Try again")
            else :
                enter1= input("please Try again")
        else :
            enter1= input("please Try again")    
    else :
        enter1= input("please Try again")
    
    
          
                
print("do you want to play madlib ??")
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

     

     
