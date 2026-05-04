rows = int(input("Enter the number of row: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")
for i in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()

print("Something new")