#obtaining length and width
length = input("Enter your field's length in feet: "))
width=input("Enter your field's width in feet: "))
#converting length and width into int
length=int(length)
width=int(width)
#finding the area
area_one= length*width
area_final=area_one//43560
print("The area is",area_final,"in acres")
