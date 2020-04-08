#obtaining seconds
time_seconds=input("Enter the time in seconds: ")
time_seconds=int(time_seconds)
#computing the days,hours,minutes,and seconds
days="{0:0=2d}".format(time_seconds//86400)

hours="{0:0=2d}".format((time_seconds% 86400)//3600)

time_remaining=((time_seconds% 86400)%3600)

minutes="{0:0=2d}".format(time_remaining//60)

seconds="{0:0=2d}".format(time_remaining%60)

#output
print(days,":",hours,":",minutes,":",seconds)
