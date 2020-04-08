import math
pi= math.pi
#obtaining radius and height
circle_radius=input("Enter the radius: ")
height=input("Enter the height: ")
#converting height and radius into float
circle_radius=float(circle_radius)
height=float(height)
#finging the volume
area= pi*(circle_radius)**2
volume=round((area*height), 1)
print(volume)
