"""""
Problem 2 – Student Academic Performance Analyzer
Design a Python program to evaluate a student&#39;s academic performance.
The program should:
 Read Student Name and USN.
 Accept marks in five subjects.
 Calculate:
o Total Marks
o Percentage
o Average
 Display the student's grade based on the following criteria:
Percentage Grade
90 and above O
80–89 A+
70–79 A
60–69 B
50–59 C
Below 50 RA
Percentage Grade
Display the result in a neatly formatted report.
Concepts Covered
 Variables
 Operators
 Input/Output
 Type Casting
 Mathematical Calculations
 String Formatting
"""""
from stringprep import map_table_b3
# Accept student details
name=input("Enter Student Name: ")
usn=input("Enter USN: ")
# Accept student marks
m1=float(input("Enter Marks in  Subject 1: "))
m2=float(input("Enter Marks in  Subject 2: "))
m3=float(input("Enter Marks in  Subject 3: "))
m4=float(input("Enter Marks in  Subject 4: "))
m5=float(input("Enter Marks in  Subject 5: "))
#calculation
total=m1+m2+m3+m4+m5
print(f"Total Marks: {total}")
percentage=total/500*100 
print(f"Percentage Grade: {percentage:.2f}%")
average=total/5
print(f"Average Marks: {average:.2f}")
if percentage>=90:
    print("o grade")
elif percentage>=80 and percentage<=89:
    print("a+ grade")
elif percentage>=70 and percentage<=79:
    print("a grade")
elif percentage>=60 and percentage<=70:
    print("b grade")
elif percentage>=50 and percentage<=59:
    print("c grade")
else:
    print("RA")
    
