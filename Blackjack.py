import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def compare(u_score, c_score):
    if u_score==c_score:
        return '*****************Its A Draw*****************'
    elif u_score == 0 :
        return "*****************You Win******************"
    elif c_score==0 :
        return "*****************Computer Wins******************"
    elif u_score>21:
        return "*****************User Went Above 21,Computer Wins******************"
    elif c_score>21:
        return "*****************Computer Went Above 21,You Win******************"
    elif c_score>u_score:
        return "*****************Computer Wins******************"
    else:
        return "*****************You Win******************"


user_card=[]
computer_card=[]
game_over=False

def deal_card():
    card=random.choice(cards)
    return card

def calculate_score(cards_uc):

    if sum(cards_uc)==21 and len(cards_uc)==2:
        return 0

    if 11 in cards_uc and sum(cards_uc)>21:
        cards_uc.remove(11)
        cards_uc.append(1)

    return sum(cards_uc)


for i in range (2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


while not game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"Your Cards Are: {user_card} , Current Score : {user_score}")
    print(f"Computer Card Is : {computer_card[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
        game_over=True
    else:
        more_card = int(input("Do You Want To Draw More Card \n"
                              "1.Yes\n"
                              "2.No : "))
        if more_card == 1:
            user_card.append(deal_card())
        else:
            game_over=True

while computer_score!=0 and computer_score<17:
    computer_card.append(deal_card())
    computer_score=calculate_score(computer_card)

print(f"Your Final Hand {user_card} , Score is {user_score}")
print(f"Your Final Hand {computer_card} , Score is {computer_score}")
print(compare(user_score,computer_score))



