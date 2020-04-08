import math
pi= math.pi
circle_radius=float(input("Enter the radius: "))
height=float(input("Enter the height: "))
area= pi*(circle_radius)**2
volume=round((area*height), 1)
print(volume)
