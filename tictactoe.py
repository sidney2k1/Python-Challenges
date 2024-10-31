theboard={"7":" ","8":" ","9":" ","4":" ","5":" ","6":" ","1":" ","2":" ","3":" ",}
boardkey=[]
for key in theboard:
    boardkey.append(key)
def printboard(board):
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    print("-+-+-")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-+-+-")
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
def game():
    turn="x"
    count=0
    for i in range(10):
        printboard(theboard)
        print("its your turn"+turn+"Move to which place?")
        move=input()
        if theboard[move]==" ":
            theboard[move]=turn
            count+=1
        else:
            print("that place i already fileed.\nMove to another place")
            continue
        if count>=5:
            if theboard["7"]==theboard["8"]==theboard["9"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["4"]==theboard["5"]==theboard["6"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["1"]==theboard["2"]==theboard["3"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["7"]==theboard["4"]==theboard["1"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["5"]==theboard["8"]==theboard["2"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["3"]==theboard["6"]==theboard["9"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["7"]==theboard["5"]==theboard["3"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
            elif theboard["1"]==theboard["5"]==theboard["9"]!=" ":
                printboard(theboard)
                print("\nGame Over")
                print("*****"+turn+"won.*****")
                break
        if count==9:
            print("Its a tie")
            print("Game over")
        if turn=="x":
            turn="o"
        else:
            turn="x"
    restart=input("Do you want to play again?(y/n)")
    if restart=="y" or restart=="Y":
        for key in boardkey:
            theboard[key]=" "
        game()
if __name__=="__main__":
    game()



