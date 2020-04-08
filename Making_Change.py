#obtaining the money
money=int(input("Enter the amount in cents: "))
#number of toonies
dollar=(money/100)
toonies=dollar//2
print(toonies,"toonies")
#number of loonies
dollars_remaining= dollar% 2
loonies=(dollars_remaining//1)
print(loonies,"loonies")
#number of quarters
cents=(dollars_remaining%1)*100
quarters=cents//25
print(quarters,"quarters")
#number of dimes
dimes=((cents%25)//10)
print(dimes,"dimes")
#number of nickels
cents_remaining=((cents%25)%10)
nickels=(cents_remaining//5)
print(nickels,"nickels")
#number of pennies
pennies=((cents_remaining%5)//1)
print(pennies,"pennies")
