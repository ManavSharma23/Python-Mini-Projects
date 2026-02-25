import random

letters=['a','b','c','d','e','f','g','h','i','j'
         ,'k','l','m','n','o','p','q','r','s','t'
         ,'u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J'
         ,'K','L','M','N','O','P','Q','R','S','T'
         ,'U','V','W','X','Y','Z']
numbers=[0,1,2,3,4,5,6,7,8,9]
signs=['!','@','#','$','%','&','*','(',')']

which_way=int(input("Would Like you create your own or programs "
                    "create for you \n"
                    "1.Your Own \n"
                    "2.Let Program Create it : "))

def own():
    password=[]
    letters_no=int(input("How Many Letters Do you want : "))
    numbers_no=int(input("How many numbers do you want : "))
    signs_no=int(input("How many signs do you want : "))

    for i in range(0,letters_no):
        letter=random.choice(letters)
        password.append(letter)

    for i in range(0,numbers_no):
        number=random.choice(numbers)
        password.append(number)

    for i in range(0,signs_no):
        sign=random.choice(signs)
        password.append(sign)

    random.shuffle(password)

    generated_password=''
    for i in password:
        generated_password+=str(i)

    print("Your Generated Password is : ",generated_password)


def computer_generated():
    password=[]
    length=int(input("Enter The length of password you want : "))
    #13
    letter_length=random.randint(0,length)     #7
    length=length-letter_length                #6
    number_length=random.randint(0,length)      #4
    length=length-number_length                #2

    for i in range(0,letter_length):
        letter=random.choice(letters)
        password.append(letter)

    for i in range(0,number_length):
        number=random.choice(numbers)
        password.append(number)

    for i in range(0,length):
        sign=random.choice(signs)
        password.append(sign)

    random.shuffle(password)

    generated_password = ''
    for i in password:
        generated_password += str(i)

    print("Your Generated Password is : ", generated_password)


if which_way ==1:
    own()
elif which_way==2:
    computer_generated()
else:
    print("Wrong Value")
