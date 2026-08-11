"""""
Problem 3 – Personal Utility Toolkit
Develop a menu-driven Python application that performs any four of the following utilities.
========== PERSONAL UTILITY TOOL ==========
1. Celsius to Fahrenheit Conversion
2. Fahrenheit to Celsius Conversion
3. Calculate Area of Circle
4. Calculate Area of Rectangle
5. Calculate Simple Interest
6. Calculate Body Mass Index (BMI)
7. Exit
The program should:
 Display a menu repeatedly.
 Accept the user&#39;s choice.
 Perform the selected operation.
 Continue until the user selects Exit.
"""""
import math
while True:
    print("1. Celsius to Fahrenheit Conversion")
    print("2. Celsius to Fahrenheit Conversion")
    print("3. Calculate Area of Circle")
    print("4. Calculate Area of Rectangle")
    print("5. Calculate Simple Interest")
    print("6. Calculate Body Mass Index (BMI)")
    print("7. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        celsius=float(input("Enter temperature in Celsius: "))
        f=(celsius*9/5)+32
        print(f"The temperature in Fahrenheit is {f}")
    elif choice==2:
        f=float(input("Enter temperature in Fahrenheit: "))
        celsius=(f-32)*5/9
        print(f"The temperature in Celsius is {celsius:.2f}")
    elif choice==3:
        r=float(input("Enter radius: "))
        area=math.pi*r*r
        print(f"The area of the circle is: {area}")
    elif choice==4:
        l=float(input("Enter length: ")) 
        b=float(input("Enter breath: "))
        area=l*b
        print(f"The area of the circle is: {area}")
    elif choice==5:
        p=float(input("Enter principle: "))
        t=float(input("Enter time: (years) "))
        rate=float(input("Enter rate: "))
        si=(p*t*rate)/100
        print(f"Simple interest is: {si}")
    elif choice==6:
        height=float(input("Enter height(cm): "))
        weight=float(input("Enter weight:(kg) "))
        bmi=weight/(height*height)
        print(f"BMI is: {bmi}")
    elif choice==7:
        print("exiting program")
        break
    else:
        print("Invalid choice")
