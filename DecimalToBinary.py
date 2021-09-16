def decimalToBinary(decimal):
    for i in range(7,-1,-1):
        k=(decimal>>i)
        if (k&1):
            print("1", end = "")
        else: 
            print("0", end = "")
decimal = int(input("Enter your decimal number: "))
if (decimal<0):
    print("Enter number between 0-255")
elif (decimal>255):
    print("Enter number between 0-255")
else:
    decimalToBinary(decimal)

        









