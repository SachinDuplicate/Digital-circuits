def first_AND (a,b):
    print ("After completing this gate, return to solve XOR gate")
    if a==1 and b==1:
        AND = 1
        print(a,"&",b,"=" ,AND)
        gate_path_A()
    elif a==1 and b==0:
        AND = 0
        print(a,"&",b,"=" ,AND)
        gate_path_A()
    elif a==0 and b==1:
        AND = 0
        print(a,"&",b,"=" ,AND)
        gate_path_A()
    elif a==0 and b==0:
        AND = 0
        print(a,"&",b,"=" ,AND)
        gate_path_A()
    else:
        print("AND gate error")

def XOR_A (a,b):
    print ("After completing this gate, return to solve AND gate")
    if a==0 and b==0:
        XOR =0
        print (a, "^", b, "=", XOR)
        gate_path_A()
    elif a==1 and b==0:
        XOR = 1
        print(a,"^",b,"=", XOR)
        gate_path_A()
    elif a==0 and b==1:
        XOR = 1
        print(a,"^",b,"=", XOR)
        gate_path_A()
    elif a==1 and b==1:
        XOR = 0
        print(a,"^",b,"=", XOR)
        gate_path_A()
    else:
        print("XOR gate error")
        
def second_AND (XOR,PREV):
    print ("After completing this gate, return to solve OR and NAND gate")
    if XOR==1 and PREV==0:
        AND_2nd = 1
        print(XOR,"&",PREV,"=" ,AND_2nd)
        gate_path_B()
    elif XOR==0 and PREV==0:
        AND_2nd = 0
        print(XOR,"&",PREV,"=" ,AND_2nd)
        gate_path_B()
    else:
        print("second_AND gate error")
        

        
def OR_A (XOR,PREV):
    print ("After completing this gate, return to solve solve NAND gate")
    if XOR==0 and PREV==0:
        OR =0
        print (XOR, "|", PREV, "=", OR)
        gate_path_C()
    elif XOR==1 and PREV==0:
        OR = 1
        print(XOR,"|",PREV,"=", OR)
        gate_path_C()
    else:
        print("OR gate error")

def NAND_A (XOR,PREV):
    print ("After completing this gate, return to solve second_AND gate")
    if XOR==0 and PREV==0:
        NAND =1
        print (XOR, "NAND", PREV, "=", NAND)
        gate_path_C()
    elif XOR==1 and PREV==0:
        NAND = 1
        print(XOR,"NAND",PREV,"=", NAND)
        gate_path_C()
    else:
        print("NAND gate error")

def third_AND (OR,NAND):
    print ("After completing this gate, return to solve OR and NAND gate")
    if OR==1 and NAND==1:
        SUM = 1
        print(OR,"&",NAND,"=" ,SUM)
        gate_path_D()
    elif OR==0 and NAND==1:
        SUM = 0
        print(OR,"&",NAND,"=" ,SUM)
        gate_path_D()
    else:
        print("third_AND gate error")


def NOR_A (AND,AND_2nd):
    print ("After the complete of this gate it send it's output to NOT gate to complete byte adder")
    if AND==0 and AND_2nd==0:
        NOR = 1
        print (AND, "NOR", AND_2nd, "=", NOR)
    elif AND==1 and AND_2nd==0:
        NOR = 0
        print(AND,"NOR",AND_2nd,"=", NOR)
    else:
        print("NOR gate error")
        
def NOT_A (NOR):
    print ("Complete of byte adder and return to start")
    if NOR==0:
        NEXT=1
        print(NOR,"~:" ,NEXT)
        Loop()
    elif NOR==1:
        NEXT=0
        print(NOR,"~:" ,NEXT)
        Loop()
    else:
        print("NOT gate error")

        
def Loop():
    x=int(input("Press 1 to solve set of gates or press 2 to exit: "))
    return x

a=None
while a is None:
    try:
        a=int(input("Enter 1 or 0:"))
    except ValueError:
        print("You are allowed to enter either 1 or 0")
print(str(a));

b=None
while b is None:
    try:
        b=int(input("Enter 1 or 0: "))
    except ValueError:
        print("You are allowed to enter either 1 or 0")
print(str(b));


def gate_path_A():
    print("Press 1 to solve AND gate and 2 to solve XOR gate or 3 to set gate path B")
    x=int(input("Enter 1/2/3: "))
    if x==1:
        first_AND (a,b)
    elif x==2:
        XOR_A (a,b)
    elif x==3:
        gate_path_B()
    else:
        print("Press 1,2 or 3")
    gate_path_A()


PREV=None
while PREV is None:
    try:
        PREV=0
    except ValueError:
        print("We have nothing to stored in the first place so input is 0")
print("Input for the previos value is: " ,PREV)


XOR=None
if a==0 and b==0:
    XOR=0
    print("Output from 1st XOR gate is:" ,XOR)
elif a==1 and b==1:
    XOR=0
    print("Output from first XOR gate is:" ,XOR)
elif a==1 and b==0:
    XOR=1
    print("Output from first XOR gate is:" ,XOR)
elif a==0 and b==1:
    XOR=1
    print("Output from first XOR gate is:" ,XOR)
else:
    print("Make sure your input number is 1 or 0")


def gate_path_B():
    print ("Press 1 to solve second_AND or press 2 to solve gate path C")
    y=int(input("Enter 1 or 2: "))
    if y==1:
        second_AND (XOR,PREV)
    elif y==2:
        gate_path_C()
    else:
        print("Enter number 1 or 2")
        gate_path_B()


AND=None
if a==1 and b==1:
    AND=1
    print("output of the first AND is" ,AND)
elif a and b:
    AND= 0
    print("Output of the first AND gate is" ,AND)
else:
    print("Make sure your input number is 1 or 0")


AND_2nd=None
if XOR==0 and PREV==0:
    AND_2nd = 0
    print("Output from the second AND gate is:" ,AND_2nd)
elif XOR==1 and PREV==0:
    AND_2nd = 0
    print("Output from the second AND gate is:" ,AND_2nd)
else:
    print("Make sure your input number is 1 or 0")


def gate_path_C():
    print("Enter 1 to solve OR or 2 to solve NAND, or 3 for the sum of bits and 4 to set fianl  gate")
    z=int(input("Press number 1/2/3/4: "))
    if z==1:
        OR_A (XOR,PREV)
    elif z==2:
        NAND_A (XOR,PREV)
    elif z==3:
        third_AND (OR,NAND)
    elif z==4:
        gate_path_D()
    else:
        print("Press 1,2,3 or 4")
        gate_path_C() 
    
OR = None
if XOR==0 and PREV==0:
    OR = 0
    print("Output from the OR gate is:" ,OR)
elif XOR==0 and PREV==0:
    OR = 1
    print("Output from the OR gate is:" ,OR)
else:
    print("Make sure your input number is 1 or 0")

NAND = None
if XOR==0 and PREV==0:
    NAND = 1
    print("Output from the NAND gate is:" ,NAND)
elif XOR==1 and PREV==0:
    NAND = 1
    print("Output from the NAND gate is:" ,NAND)
else:
    print("Make sure your input number is 1 or 0")

SUM = None
if OR==1 and NAND==1:
    SUM = 1
    print("Finally sum of the bit adder is:", SUM)
elif OR==0 and NAND==1:
    SUM = 0
    print("Finally sum of the bit adder is:", SUM)
else:
    print("Make sure your input number is 1 or 0")

def gate_path_D():
    print("Press 1 to get NOR and NOT gate and 2 for the sum of bits")
    Z=int(input("Press 1/2: "))
    if Z==1:
        NOR_A(AND,AND_2nd)      
    else:
        print("Press 1 or 2")
        gate_path_D

    print("NOT gate will store the final output in variable named NEXT")
    NOT_A (NOR)


NOR = None
if AND==0 and AND_2nd==0:
    NOR = 1
    print("Output from the NOR gate is:" ,NOR)
elif AND==1 and AND_2nd==0:
    NOR = 1
    print("Output from the NOR gate is:" ,NOR)
else:
    print("Make sure your input number is 1 or 0")

      
Resume = 1
while Resume == 1:
    LP = Loop()
    if LP == 1:
        print("Byte adder processing")
        gate_path_A()
    elif LP == 2:
        print("Byte Adder exit")
        exit()
    else:
        print("Type a valid number")
        Loop()
