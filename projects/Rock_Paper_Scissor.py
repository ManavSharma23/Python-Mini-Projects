import random

rock="""    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

drawings=[rock,paper,scissor]

user_choice=int(input("Enter Your Choice \n"
                      "0.Rock \n"
                      "1.Paper \n"
                      "2.Scissor : "))

computer_choice=random.randint(0,2)
print(f"Your Choice :\n"
      f"     "
          f"{drawings[user_choice]}")
#____________________________________________________________#
print(f"computer Choice is :\n"
      f" {drawings[computer_choice]}")

if user_choice==computer_choice:
    print("Draw")
elif user_choice==0 and computer_choice==1:
    print("Computer Wins")
elif user_choice==0 and computer_choice==2:
    print("You Win")
elif user_choice==1 and computer_choice==2:
    print("Computer Win")
elif user_choice==1 and computer_choice==0:
    print("You Win")
elif user_choice==2 and computer_choice==0:
    print("Computer Win")
elif user_choice==2 and computer_choice==1:
    print("You Win")
else:
    print("Invalid Input")

