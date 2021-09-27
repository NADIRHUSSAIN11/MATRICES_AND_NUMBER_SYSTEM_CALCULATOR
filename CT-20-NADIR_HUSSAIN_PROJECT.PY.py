print("************************************************************")
print("**********(Matrices And Number System Calculator)***********\t\t")
print("************************************************************\n")
a=int(input("FOR ADDITION OF MATRIX PUT (1)\n\nFOR SUBSTRACTION OF MATRIX PUT (2)\n\nFOR MULTIPLICATION OF MATRIX PUT (3)\n\nFOR NUMBER SYSTEM PUT (4)\n\nEnter : "))
import NumberSystem as NS 
if a==1:
    row=int(input("ENTER THE NUMBER OF ROWS HERE : "))
    col=int(input("ENTER THE NUMBER OF COLUMNS HERE : "))

    print("ENTER THE ELEMENTS FOR MATRIX 1 : ")
    MATRIX1=[[int(input()) for i in range(col)] for j in range(row)]
    print("MATRIX 1 :")
    for i in range(row):
        for j in range(col):
            print(format(MATRIX1[i][j],"<3"),end=" ")
        print()

    print("ENTER THE ELEMENTS FOR MATRIX 2 : ")
    MATRIX2=[[int(input()) for i in range(col)] for j in range(row)]
    print("MATRIX 2 : ")
    for i in range(row):
        for j in range(col):
            print(format(MATRIX2[i][j],"<3"),end=" ")
        print()
    result=[[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j]=MATRIX1[i][j]+MATRIX2[i][j]
    print("The Result of Addition is : ")
    for i in range(row):
        for j in range(col):
            print((result[i][j]),end="  ")
        print()
elif a==2:
    row=int(input("ENTER THE NUMBER OF ROWS HERE : "))
    col=int(input("ENTER THE NUMBER OF COLUMNS HERE : "))

    print("ENTER THE ELEMENTS FOR MATRIX 1 : ")
    MATRIX1=[[int(input()) for i in range(col)] for j in range(row)]
    print("MATRIX 1 : ")
    for i in range(row):
        for j in range(col):
            print(format(MATRIX1[i][j],"<3"),end=" ")
        print()

    print("ENTER THE ELEMENTS FOR MATRIX 2 : ")
    MATRIX2=[[int(input()) for i in range(col)] for j in range(row)]
    print("MATRIX 2 : ")
    for i in range(row):
        for j in range(col):
            print(format(MATRIX2[i][j],"<3"),end=" ")
        print()
    result=[[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j]=MATRIX1[i][j]-MATRIX2[i][j]
    print("The Result of Substraction is : ")
    for i in range(row):
        for j in range(col):
            print((result[i][j]),end="  ")
        print()
elif a == 3 :
    row = int(input("Enter Row for Matrix(1) : ")) 
    col = int(input("Enter Column for Matrix(2) : "))
    com = int(input("Enter Column for Matrix(1)/Enter Row for Matrix(2) : "))
    print("Enter Elements for Matrix(1) in row order : ")
    matrix1 = [[int(input()) for i in range(com)] for j in range(row)]
    print("Matrix(1) : ")
    for i in range(row) :
        for j in range(com) :
            print(format(matrix1[i][j],"<5"),end="")
        print()
    print("Enter Elements for Matrix(2) in row order : ")
    matrix2 = [[int(input()) for i in range(col)] for j in range(com)]
    print("Matrix(2) : ")
    for i in range(com) :
        for j in range(col) :
            print(format(matrix2[i][j],"<5"),end="")
        print()
    result = [[0 for i in range(col)] for j in range(row)]
    for i in range(row) :
        for j in range(col) :
            for k in range(com) :
                result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]
    print("Result of Multiplication is : ")
    for i in range(row) :
        for j in range(col) :
            print(format(result[i][j],"<5"),end="")
        print()
elif a == 4 :
    print("(1) Binary To Decimal\n(2) Decimal To Binary\n(3) Decimal To Hexadecimal\n(4) Hexadecimal To Decimal")
    b  = int(input("Enter : "))
    if b == 1 :
        NS.bintodec()
    elif b == 2 :
        NS.dectobin()
    elif b == 3 :
        NS.dectohex()
    elif b == 4 :
        NS.hextodec()
    else :
        print("Invalid Input\nTry Again Please !")
else :
    print("Invalid Input\nTry Again Please !")    



