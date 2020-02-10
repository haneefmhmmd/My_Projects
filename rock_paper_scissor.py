import random
cond=0
list=['rock','paper','scissor']
user_point,comp_point=0,0
print("Press one to exit")
while cond<5:
    user_input=input("rock or paper or scissor: ")
    if user_input not in list and not '1':
        print("Wrong input")
        cond=0
    if user_input=='1':
        print("Thank you for playing!")
        break
    random_input=random.choice(list)
    print("computer input: ",random_input)
    if user_input==random_input:
        user_point+=1
    else:
        comp_point+=1
    if cond==4:
        if user_point>comp_point:
            print("You Win")
        elif comp_point>user_point:
            print("Computer Win")
        else:
            print("Draw")
    cond+=1
