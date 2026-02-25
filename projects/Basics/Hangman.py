import random

HANGMANPICS = [

'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 +---+
 |   |
     |
     |
     |
     |
========='''
               ]


word_list = [
    "apple","banana","orange","grapes","mango","peach","cherry","lemon","papaya","guava",
    "coffee","tea","sugar","butter","bread","cheese","pizza","burger","pasta","noodles",
    "school","college","teacher","student","pencil","eraser","notebook","marker","chalk",
    "temple","church","mosque","palace","castle","museum","library","stadium","airport",
    "railway","station","ticket","travel","journey","holiday","picnic","vacation",
    "python","java","coding","program","laptop","mobile","keyboard","screen","internet",
    "network","server","router","signal","battery","charger","camera","speaker","mouse",
    "animal","tiger","lion","elephant","monkey","rabbit","donkey","zebra","giraffe",
    "planet","earth","mars","venus","jupiter","saturn","galaxy","universe","meteor",
    "cricket","football","hockey","tennis","badminton","kite","stadium","umpire",
    "music","guitar","piano","violin","drums","flute","artist","singer","concert",
    "friend","family","mother","father","brother","sister","cousin","uncle","aunt",
    "summer","winter","monsoon","spring","autumn","season","weather","climate",
    "mountain","river","ocean","forest","desert","island","valley","waterfall"
]

chosen_word=random.choice(word_list)

placeholder=''

for i in chosen_word:
    placeholder+='_'

print(placeholder)


guessed_letters=[]
lives=6

game_over=False

while not game_over:
    print("**********************You Have ", lives, " chances left *************************")
    guess = input("Enter Your Guess : ").lower()
    guessing_word = ''

    if guess in guessed_letters:
        print("You Have Already guessed this letter")

    for letter in chosen_word:
        if letter==guess:
            guessing_word+=letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            guessing_word+=letter
        else:
            guessing_word+='_'


    if guess not in chosen_word:
        lives-=1
        print("Wrong Guess")
        if lives==0:
            print("Game Over")
            game_over=True
            print("+++++++++++++++ YOU LOSE ++++++++++++++++")
            print("Correct Word Was : ",chosen_word)

        else:
            pass


    if '_' not in guessing_word:
        print("++++++++++++++ YOU WIN +++++++++++++++++")
        game_over=True
    else:
        pass


    print(guessing_word)
    print(HANGMANPICS[lives])



