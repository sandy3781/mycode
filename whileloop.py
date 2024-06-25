#!/usr/bin/python3

round = 0
while True:
    round = round+1
    print("finish the title, pythons life ")
    answer=input("you guess is ...")
    answer=answer.lower()
    if answer == "brian":
        print("correct")
        break
    elif round == 3:
        print("answer is not Brian")
        break
    else:
        print("sorry try again")
