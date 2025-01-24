def word_counter():
    text = input("Enter a block of text: ")         # Output: Enter a block of text: My name is Ahnaf Mahmud Towseem Ahan, and I am currently a student of Class 10 EV, 
                                                        #     Science Department at Willes Little Flower School and College.
    words = text.split()
    print(f"Word Count: {len(words)}")              # Output: Word Count: 26

    word_counter()
