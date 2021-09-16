def BinaryToDeciaml():
    binary = list(input("Enter your binary number: "))
    decimal = 0

    for i in range(len(binary)):
            digit = binary.pop()
            if digit == '1':
                    decimal = decimal + pow(2, i)
    if (decimal<0):
        print("You are allowed to enter 00000000 mimum")
    elif (decimal>255):
        print("You are allowed to enter only upto 11111111")
    else:
        print("The decimal value of the number is", decimal)
BinaryToDeciaml()
