from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

today = date.today()
print('today: {0!s}'.format(today))
print('{0!s}'.format(today.year))
print('{0!s}'.format(today.month))
print('{0!s}'.format(today.day))
current_datetime = datetime.today()
print('{0!s}'.format(current_datetime))

one_today = timedelta(days=-1)
yesterday = today + one_today
print('yesterday : {0!s}'.format(yesterday))
neight = timedelta(hours=-8)
print('outprint:{0!s}'.format(neight.days, neight.seconds))

date_diff = today - yesterday
print('outprint:{0!s}'.format(date_diff))
print('output:{0!s}'.format(str(date_diff).split()[0]))

print('output:{0!s}'.format(today.strftime('%m/%d/%Y')))
print('output:{0!s}'.format(today.strftime('%b %d, %Y')))
print('output:{0!s}'.format(today.strftime('%Y-%m-%d')))
print('output:{0!s}'.format(today.strftime('%B %d, %Y')))

print('outprint:{0!s}'.format(datetime.date(datetime.strftime(date, '%Y-%m-%d'))))
print('outprint:{0!s}'.format(datetime.date(datetime.strftime(date, '%B %d, %Y'))))
