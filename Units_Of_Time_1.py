#obtaining days,hours,minutes,seconds
days=int(input("Enter the number of days: "))
hours=int(input("Enter the number of hours: "))
minutes=int(input("Enter the amount of minutes: "))
seconds=int(input("Enter the amount of seconds: "))
#obtaining the seconds
time_seconds=((days*86400)+(hours*3600)+(minutes*60)+seconds)
#output
print("The time in seconds is",time_seconds)     
