from os import system

def printOPtions ():
    print("0. Append item to the list")
    print("1. Check if an item is in the list")
    print("2. Delete item from the list")
    print("3. Print list")
    print("Q. to exit")

def appnditem (arr: list):
    append = input("Insert the item you want to append then press enter:\n")
    if append in arr:
        print("The item is already in the list")
    else:
        ans = input("Are you sure you want to add " + append + " to the list (Y/N):\n")
        if ans == "Y" or ans == "y":
            arr.append(append)
            print("The item has been added to the list")
        else:
            print("Nothing has happen to the list")

def checkitem(arr: list):
    ans = input("Which item do you want to check:\n")
    if ans in arr:
        print("The item is in the list")
    else:
        print("The item is not in the list")

def delitem (arr: list):
    item = input("Which item do you want to delete:\n")
    if item in arr:
        ans = input("Are you sure you want to delete " + item + " from the list? (Y/N):\n")
        if ans == "Y" or ans == "y":
            arr.remove(item)
            print("The item has been deleted from the list")
        else:
            print("Nothing has happen to the list")
    else:
        print("The item " + item + " is not in the list")

def printlist(arr: list):
    if arr == []:
        print("The list is empty")
    else:
        print("The items in the list are:\n")
        for x in arr:
            print(x)
        print("\n")

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
            case "0":
                appnditem(arr)
            case "1":
                checkitem(arr)
            case "2": 
                delitem(arr)
            case "3":
                printlist(arr)
            case _:
                print("Insert a valid option")
        input("Press enter to continue...")
main()