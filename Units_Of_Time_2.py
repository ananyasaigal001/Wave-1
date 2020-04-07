time_seconds=int(input("Enter the time in seconds: "))

days="{0:0=2d}".format(time_seconds//86400)

hours="{0:0=2d}".format((time_seconds% 86400)//3600)

time_remaining=((time_seconds% 86400)%3600)

minutes="{0:0=2d}".format(time_remaining//60)

seconds="{0:0=2d}".format(time_remaining%60)

print(days,":",hours,":",minutes,":",seconds)
