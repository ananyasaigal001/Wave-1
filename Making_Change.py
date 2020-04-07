money=int(input("Enter the amount in cents: "))
dollar=(money/100)
toonies=dollar//2
print(toonies,"toonies")
dollars_remaining= dollar% 2
loonies=(dollars_remaining//1)
print(loonies,"loonies")
cents=(dollars_remaining%1)*100
quarters=cents//25
print(quarters,"quarters")
dimes=((cents%25)//10)
print(dimes,"dimes")
cents_remaining=((cents%25)%10)
nickels=(cents_remaining//5)
print(nickels,"nickels")
pennies=((cents_remaining%5)//1)
print(pennies,"pennies")
