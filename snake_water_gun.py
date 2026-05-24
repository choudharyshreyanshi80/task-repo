import random

l = ['snake', 'water', 'gun']

ch=int(input('''Game start....
             1.Yes
             2.No'''))

if ch==1:

    user_score=0
    computer_score=0

    for a in range(5):
        uch=input("User choice:")
        cch = random.choice(l)
        print("Computer choice:",cch)

        if cch==uch:
            print("Match draw...")
            user_score+=1
            computer_score+=1

        elif((cch=='snake' and uch=='gun')or
             (cch=='water' and uch=='snake')or 
             (cch=='gun' and uch=='water')):
            user_score+=2
            print("You win.....")

        else:
            computer_score+=2
            print("Computer wins...")

    if user_score==computer_score:
        print("Draw..")
    elif user_score>computer_score:
        print("You won the match..")
    else:
        print("Computer won the match..")

else:
    print("Invalid!!!")


    
    
    
