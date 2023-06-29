mounts = {"Adamantoise Whistle": 200000, "Pod 602 Key": 300000, "Archon Throne": 750000,
              "Korpokkur Horn": 750000, "Typhon Horn": 750000, "Fenrir Horn": 1000000, "Sabotender Emperador": 2000000}

emotes = {"P. Happ.": 20000, "Thav Dance": 80000, "Gold Dance": 80000, "Unsheathe": 100000, "Sheathe": 100000}

minions = {"Water Imp":10000, "Zu Hatchling": 10000, "Black Coeurl": 20000, "Heavy Hatchling": 20000,
               "Wind-Up Nero": 30000, "Piggy": 30000, "Unlucky Rabbit": 30000}

hairstyles = {"Curls": 9600, "Lexen Tails": 50000}

def welcome():
    print("Gold Saucer Log")
    print("---------------")
    print("Hey Valentine~")
    print()

def menu():
    print("Which would you like to view?")
    print("-----------------------------")
    print("Mounts:\t\tDisplays list of mounts and their MGP cost")
    print("Emotes:\t\tDisplays list of emotes and their MGP cost")
    print("Minions:\tDisplays list of minions and their MGP cost")
    print("Hair:\t\tDisplays list of hairstyles and their MGP cost")
    print("Total:\t\tDisplays combined total of all GS items")
    print("Add:\t\tAdd an item to a category")
    print("Remove:\t\tRemoves an item from a category")
    print("Exit:\t\tExit program")
    print()


def display_mounts(mounts):
    for key, value in mounts.items():
        print(f"{key}:\t{value}")
    print("Total:\t{:,}".format(sum(mounts.values())), "MGP")

def display_emotes(emotes):
    for key, value in emotes.items():
        print(f"{key}:\t{value}")
    print("Total:\t\t{:,}".format(sum(emotes.values())), "MGP")

def display_minions(minions):
    for key, value in minions.items():
        print(f"{key}:\t{value}")
    print("Total:\t{:,}".format(sum(minions.values())), "MGP")

def display_hairstyles(hairstyles):
    for key, value in hairstyles.items():
        print(f"{key}:\t{value}")
    print("Total:\t{:,}".format(sum(hairstyles.values())), "MGP")

def grand_total(mounts, emotes, minions, hairstyles):
    total = sum(mounts.values())
    total += sum(emotes.values())
    total += sum(minions.values())
    total += sum(hairstyles.values())
    print("Grand total: {:,}".format(total), "MGP")

def add_item():
    while True:
        category = input("What category do you want to add an item to? (type 'Exit' to leave this submenu): ")
        if category.lower() == "mounts":
            name = input("Enter the name of the item: ")
            amount = int(input("Enter the amount of MGP the item costs: "))
            mounts.update({name: amount})
            print(name + " has been added!")
        elif category.lower() == "emotes":
            name = input("Enter the name of the item: ")
            amount = int(input("Enter the amount of MGP the item costs: "))
            emotes.update({name: amount})
            print(name + " has been added!")
        elif category.lower() == "minions":
            name = input("Enter the name of the item: ")
            amount = int(input("Enter the amount of MGP the item costs: "))
            minions.update({name: amount})
            print(name + " has been added!")
        elif category.lower() == "hair":
            name = input("Enter the name of the item: ")
            amount = int(input("Enter the amount of MGP the item costs: "))
            hairstyles.update({name: amount})
            print(name + " has been added!")
        elif category.lower() == "exit":
            break
        else:
            print("Invalid command\n")
        print()

def remove_item():
    while True:
        category = input("What category do you want to remove an item from? (type 'Exit' to leave this submenu): ")
        if category.lower() == "mounts":
            name = input("Enter the name of the item: ")
            if mounts.get(name):
                mounts.pop(name)
                print(name + " has been removed!")
            else:
                print("Item not found")
        elif category.lower() == "emotes":
            name = input("Enter the name of the item: ")
            if emotes.get(name):
                emotes.pop(name)
                print(name + " has been removed!")
            else:
                print("Item not found")
        elif category.lower() == "minions":
            name = input("Enter the name of the item: ")
            if minions.get(name):
                minions.pop(name)
                print(name + " has been removed!")
            else:
                print("Item not found")
        elif category.lower() == "hair":
            name = input("Enter the name of the item: ")
            if hairstyles.get(name):
                hairstyles.pop(name)
                print(name + " has been removed!")
            else:
                print("Item not found")
        elif category.lower() == "exit":
            break
        else:
            print("Invalid command\n")
        print()

def main():
    welcome()
    while True:
        menu()
        command = input("Command: ")
        if command.lower() == "mounts":
            display_mounts(mounts)
        elif command.lower() == "emotes":
            display_emotes(emotes)
        elif command.lower() == "minions":
            display_minions(minions)
        elif command.lower() == "hair":
            display_hairstyles(hairstyles)
        elif command.lower() == "total":
            grand_total(mounts, emotes, minions, hairstyles)
        elif command.lower() == "add":
            add_item()
        elif command.lower() == "remove":
            remove_item()
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command\n")
        print()

    print("Good luck getting all your MGP!")


if __name__ == "__main__":
    main()