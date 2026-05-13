# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use")

for x in range(rows):
    for y in range(columns): #inner counter must be different than outer, so y instead of x
        print(symbol, end = "")
    print()