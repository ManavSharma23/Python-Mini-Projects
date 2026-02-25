letters=['a','b','c','d','e','f','g','h','i','j'
         ,'k','l','m','n','o','p','q','r','s','t'
         ,'u','v','w','x','y','z',]

def option():
    directon = int(input("What Do You Want To Do  \n"
                     "1.Encode\n"
                     "2.Decode : "))
    text = input("Enter The Text : ")
    shift = int(input("Enter The Shift Number : "))
    if directon==1:
        encrypt(original_text=text,shift_number=shift)
    elif directon==2:
        decrypt(original_text=text,shift_number=shift)
    else:
        print("Wrong Input")

    choice=int(input("Do You want to do it again ? \n"
                     "1.Yes\n"
                     "2.No : "))
    if choice==1:
        print("Starting Again")
        option()
    elif choice==2:
        print("Exiting Code")
    else:
        print("Wrong Input Given")
        print("Exiting Code")

def encrypt(original_text,shift_number):
    cipher_text=""
    for i in original_text:
        if i in letters:
            shifted_index=letters.index(i)+shift_number
            shifted_index%= len(letters)
            cipher_text+=letters[shifted_index]
        else:
            cipher_text+=i
    print("Encoded Text : ",cipher_text)



def decrypt(original_text,shift_number):
    cipher_text=""
    # hello
    for i in original_text:
        if i in letters:
            shifted_index=letters.index(i)-shift_number
            cipher_text+=letters[shifted_index]
        else:
            cipher_text+=i

    print("Decoded Text : ",cipher_text)


option()




