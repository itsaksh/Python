""""
Problem 1 – Smart Shopping Bill Generator
A supermarket wants to automate its billing process.
Develop a Python program that:
 Accepts the customer&#39;s name.
 Accepts the names and prices of three products.
 Calculates the total amount.
 If the total amount exceeds ₹3000, provide a 10% discount.
 Display:
o Customer Name
o Product Details
o Total Amount
o Discount
o Final Payable Amount
"""
# Accept customer details
name=input("Enter your name: ")
n1=input("Enter name of product 1: ")
n2=input("Enter name of product 2: ")
n3=input("Enter name of product 3: ")
p1=int(input("Enter price of item 1: "))
p2=int(input("Enter price of item 2: "))
p3=int(input("Enter price of item 3: "))
#calculation
totalamt=p1+p2+p3
print(f"total amt= {p1} + {p2} + {p3} = {totalamt}") #total amt=p1+p2+p3
if totalamt>3000:
    d=totalamt*10/100 #discount=total amount*(discount% ÷ 100)
    print(f"discount={d}")
else:
    d=0
finalprice=totalamt-d #final  payable amt=totalamt-discount
print(f"final price={finalprice}")

