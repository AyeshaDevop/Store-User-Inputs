def main():
    """
    Continuously asks the user for input and stores values in a list
    until the user presses enter without typing anything.
    """
    lst = []  
    val = input("Enter a value: ")  
    while val: 
        lst.append(val)  
        val = input("Enter a value: ")  

    print("Here's the list:", lst)  

if __name__ == '__main__':
    main()