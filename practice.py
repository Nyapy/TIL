import datetime
date = datetime.date(2019,7,13)
print(f'{date.year}{date.month}{date.day}')

print(date.strftime('%Y%m%d'))

print(date)

for i in range(51):
   t_time = date - datetime.timedelta(weeks=i)
   targetDt = t_time.strftime('%Y%m%d')
   print(targetDt)