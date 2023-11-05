from os import system

def printOPtions ():
    print("0. Append item to the list")
    print("1. Check if an item is in the list")
    print("2. Delete item from the list")
    print("Q. to exit")

def append (arr: list):
    append = input("Insert the item you want to append then press enter:\n")
    if append in arr:
        print("The item is already in the list")
    else:
        ans = input("Are you sure you want to add " + append + " to the list (Y/N):\n")
        if ans == "Y" or ans == "y":
            arr.append(append)
            print("The item has been added to the list")

def checkitem(arr: list):
    ans = input("Which item do you want to check:\n")
    if ans in arr:
        print("The item is in the list")
    else:
        print("The item is not in the list")
        

def delitem (arr: list):
    pass

def main ():
    arr = []
    ans = ""
    while ans != "Q" and ans != "q":
        system("clear")
        printOPtions()
        ans = input("What do you want to do:\n")
        if ans == "Q" or ans == "q":
            continue
        match ans:
            case "1":
                append(arr)
            case "2":
                checkitem(arr)
            case "3": 
                pass
            case _:
                print("Insert a valid option")
        input("Press enter to continue...")
main()