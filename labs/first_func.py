#!/usr/bin/python3

def first_function():
    y = ["name1", "name2"]
    y.append("name3")
    return y  # send this back from whom called it

# second function
def second_function(x):
    #print(x) # prints ["name1", "name2"]

    #print('this is my first function')
    #name1=input("enter your name :")
    #print("welcome :",name1)
    #name2 = input("enter second name:")
    #print ("welcome :", name2)
    z = [11,12,13]

    print(dict(zip(x, z)))



def main():

    namedata = first_function()

    second_function(namedata)

    # what if we wanted to turn a list into a dictionary??
    

 
if __name__ == "__main__":    
    main()
