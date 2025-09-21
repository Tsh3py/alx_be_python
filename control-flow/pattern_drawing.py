try:
    size = int(input("Enter the size of the pattern: "))
    
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()


row = 0


while row < size:
    
    for _ in range(size):
        
        print("*", end="")
    
    print()
    
    row += 1
