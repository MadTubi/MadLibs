def story1(lst):
    lst = list(lst)
    message = f"\nThere once lived a {lst[0]} person who ate only {lst[1]}. \nOne day this person found {lst[2]} dollars and decided to trade it for a {lst[3]} {lst[4]} bucket of {lst[5]}! \nSo they ran to the {lst[6]} and asked one of the staff for the item they wanted in a to go box !\nThe staff looked {lst[7]}  but went to the back room and traded the item for the bucket of {lst[5]}.\nThey were so happy that they {lst[8]} everyone in the building.\nThen hopped on their {lst[9]} and rode off into the sunset.\n--THE END--"
    print(message)

def story2(lst):
    lst=list(lst)
    message =f"\nI was so {lst[0]} one day that I decided to go to the Zoo for fun.\nI saw {lst[1]} and {lst[2]} baby lions!\nI even saw a {lst[3]},{lst[4]} {lst[5]}. \nI then walked to the {lst[6]} to buy presents from my awesome day out. \nI bought {lst[7]} candy and a hippo toy that {lst[8]}! \nI then got in my {lst[9]} and drove away. \nI wish I could go to the zoo everyday!\n--THE END--"
    print(message)

def story3(lst):
    lst=list(lst)
    message =f"\nI once skipped school one day becasue it was so {lst[0]}.\nI jumped in my {lst[1]} and went to Bumpers. \nI ordered {lst[2]} hamburgers and milkshakes!I then started to feel {lst[3]} and {lst[4]}. \nI started my car and  floored it to the nearest {lst[6]}. \nI couldn't find a bathroom so I used it in a  {lst[5]} by the clothing store.\nI then slipped out the store as people started noticing the {lst[7]} smell coming from where I was.\nI then  {lst[8]} to my {lst[1]}  and drove off to pick up my pet {lst[9]}.\n--THE END--"
    print(message)

def main():

    myPOS = []

    adj1 = input("Enter an adjective: ")
    myPOS.append(adj1)

    noun1 = input("Enter a noun: ")
    myPOS.append(noun1)

    number = input("Enter a number: ")
    myPOS.append(number)

    adj2 = input("Enter an adjective: ")
    myPOS.append(adj2)

    adj3 = input("Enter an adjective: ")
    myPOS.append(adj3)

    noun2 = input("Enter a noun: ")
    myPOS.append(noun2)

    location = input("Enter a location: ")
    myPOS.append(location)

    adj4 =  input("Enter an adjective: ")
    myPOS.append(adj4)

    verb1 =  input("Enter a verb: ")
    myPOS.append(verb1)

    noun3 = input("Enter a noun: ")
    myPOS.append(noun3)


    menu = "\n1.Story 1\n2.Story 2\n3.Story 3"
    print(menu)
    choice = int(input("What story would you like to complete ? "))

    if choice == 1:
        print("Here is story 1:")
        story1(myPOS)

        menu_ver2="\n1.Yes\n2.No"
        print("\nWould you like to play another story?")
        print(menu_ver2)
        playAgain = int(input("Enter response here: "))

        if playAgain == 1:
            print("Which story would you like to play?")
            menu_ver3 = "\n1.Story 2\n2.Story 3"
            print(menu_ver3)
            pickStory = int(input("Pick a story:"))

            if pickStory == 1:
                print("\nHere is story 2: ")
                story2(myPOS)

            elif pickStory == 2:
                print("\nHere is story 3: ")
                story3(myPOS)

        elif playAgain == 2:
            print("You selected 'No'\nGoodbye!!")


    elif choice == 2:
        print("Here is story 2:\n")
        story2(myPOS)

        menu_ver2="\n1.Yes\n2.No"
        print("\nWould you like to play another story?")
        print(menu_ver2)
        playAgain = int(input("Enter response here: "))

        if playAgain == 1:
            print("Which story would you like to play?")
            menu_ver3 = "\n1.Story 1\n2.Story 3"
            print(menu_ver3)
            pickStory = int(input("Pick a story:"))

            if pickStory == 1:
                print("\nHere is story 1: ")
                story1(myPOS)

            elif pickStory == 2:
                print("\nHere is story 3: ")
                story3(myPOS)

        elif playAgain == 2:
            print("You selected 'No'\nGoodbye!!")



    elif choice == 3:
        print("Here is story 3:\n")
        story3(myPOS)

        menu_ver2="\n1.Yes\n2.No"
        print("\nWould you like to play another story?")
        print(menu_ver2)
        playAgain = int(input("Enter response here: "))

        if playAgain == 1:
            print("Which story would you like to play?")
            menu_ver3 = "\n1.Story 1\n2.Story 2"
            print(menu_ver3)
            pickStory = int(input("Pick a story:"))

            if pickStory == 1:
                print("\nHere is story 1: ")
                story1(myPOS)

            elif pickStory == 2:
                print("\nHere is story 2: ")
                story2(myPOS)

        elif playAgain == 2:
            print("You selected 'No'\nGoodbye!!")

    elif choice == 4:
        print("You selected 'QUIT'. Goodbye!")
    else:
        print("ERROR - Invalid input.")
main()
