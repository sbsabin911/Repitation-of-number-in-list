def call(num,temp):
    count=0
    for i in range(len(temp)):       #checking the repetation of the number in the list
        if temp[i]==num:
         count+=1
    print(f"the numebr is {num} and the repetition is {count}")   # printing the final result 

def single_number(temp):
    for i in range(len(temp)):
        call(temp[i],temp)
temp=[]
def user_input():                  # user input
    print("enter the number ")
    while True:
        number=input()
        if number=='f':             #exit user input if user press f
            break
        else:
            temp.append(number)        #adding the user input to the existing list
    single_number(temp)


user_input()
