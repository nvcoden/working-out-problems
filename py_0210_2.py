'''Write a function that takes to argument(Date, Date) to calculate number of days between two dates.
'''

from datetime import date
def function(a,b):
    day1 = date(a[0],a[1],a[2])
    day2 = date(b[0],b[1],b[2])
    return (day2-day1).days

print( function([2014, 7, 2], [2014, 7, 11]), 'days')