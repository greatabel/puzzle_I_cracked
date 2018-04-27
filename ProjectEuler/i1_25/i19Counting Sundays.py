# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def findSundays(start, end):
    print(start, end)
    import pandas as pd
    alldays = pd.date_range(start,end,freq='D')
    total = sum( theday.day == 1 and theday.weekday() == 6  for theday in alldays)
    print(total)

def showSundays(start, end):
    print(start, end)
    import pandas as pd
    alldays = pd.date_range(start,end,freq='D')

    for theday in alldays:
        if theday.day == 1 and theday.weekday() == 6:
            print(theday)

if __name__ == "__main__":
    findSundays('1901/1/1','2000/12/31') 
    showSundays('1901/1/1','2000/12/31') 