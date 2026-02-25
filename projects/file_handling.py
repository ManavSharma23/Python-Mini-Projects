with open("hello.txt",mode='r') as file:
    data=file.read()
    # l1=[]
    # for i in data:
    #     l1.append(i.split())
    #
    # count=0
    # for word in l1:
    #     for nested_word in word:
    #         print(nested_word)
    #         count+=1
    #
    #     print(count)



    data_list=data.split()
    print(data_list)
    data_word=[]
    word=input("Enter The letter : ").lower()
    data_word.append(word)
    data_word.append(word.capitalize())

    def func(data_word):
        total_count = 0
        for i in data_list:
            for j in i:
                if j in data_word:
                    total_count+=1

        return total_count



    print(func(data_word))



