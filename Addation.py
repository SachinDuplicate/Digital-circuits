def addation():
    a=int(input("Enter number between 0-255: "))
    if (a<0):
        print(a)
    elif (a<256):
        print(a)
    else:
        print("You are allowed to enter nubmber between 0 to 255")
        a=None
        addation()
    b=int(input("Enter number between 0-255: "))
    if (b<0):
        print(b)
    elif (b<256):
        print(b)
    else:
        print("You are allowed to enter nubmber between 0 to 255")
        b=None
        addation()
    SUM=a+b
    print("Sum = ",SUM)
    l=[]
    while SUM>=1:
        if SUM%2==0:
            l.append(0)
        else:
            l.append(1)
        SUM=SUM//2
    l2=l[::-1]
    print("Binary of sum =",l2)
addation()
