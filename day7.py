import datetime

Date = datetime.datetime.now()
year = Date.year
month = Date.month

days = [0,31,29 if (year%4)==0 and (year%100) !=0 or (year%400)==0 else 28 ,31,30,31,30,31,31,30,31,30,31]

print("{} days for {}-{}" .format(days[month], year, month ))


days2 = {1:31,2:29 if (year%4)==0 and (year%100) !=0 or (year%400)==0 else 28, 3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

print("{} days for {}-{}" .format(days2.get(month), year, month ))
