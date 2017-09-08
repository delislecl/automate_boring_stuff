import time
import datetime

#TIME

#Display time
time.time()

#Count time
startTime = time.time()

count=0
for i in range(1000):
    for j in range(1000):
        count += 1

endTime = time.time()

print('Took %s seconds' %(endTime-startTime))


#Sleep
time.sleep(3)


#DATEIME

#Date now
datetime.datetime.now()

#Set datetime
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day
dt.hour, dt.minute, dt.second

#Just date
datetime.date.today()

#Convert from timestamp
datetime.datetime.fromtimestamp(1000000)
datetime.datetime.fromtimestamp(time.time())

#Convert to strings
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
oct21st.strftime('%I:%M %p')
oct21st.strftime("%B of '%y")

#String to datetime
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime.strptime("October of '15", "%B of '%y")
datetime.datetime.strptime("November of '63", "%B of '%y")

#TIMEDELTA

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays