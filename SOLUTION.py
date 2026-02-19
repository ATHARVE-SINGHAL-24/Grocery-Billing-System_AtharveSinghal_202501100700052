a=float(input("Enter price of item 1 : "))     #input first item price
b=float(input("Enter price of item 2 : "))     #input second item price
c=float(input("Enter price of item 3 : "))     #input third item price

total=a+b+c   #total amount
discount=0    #initializing discount

print(f'Total cost: {total}')      

if total>50:                                #if total amount is greater than 50, then apply 10% discount
    discount=total*0.1
    print(f'Discount applied: {discount:.2f}')

final=total-discount                        #calculating final price
print(f'final amount: {final:.2f}')         #printing final price