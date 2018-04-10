# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if (year%4==0 and year%100 !=0) or year%400 = 0:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysBt = 0
    for year in range(year1, year2+1):
        if isLeapYear(year) == True:
            daysBt = daysBt + 366
        else:
            daysBt = daysBt + 365
            
    if isLeapYear(year1) ==True:
        if isLeapYear(year2) ==True:
            left = sum(days_leap[:month1-1]) + day1 
            right = sum(days_leap[month2:]) + days_leap[month2-1] - day2
            daysBt = daysBt - left - right 
        else:
            left = sum(days_leap[:month1-1]) + day1 
            right = sum(days[month2:]) + days[month2-1] - day2
            daysBt = daysBt - left - right 
    
    else:
        if isLeapYear(year2) ==True:
            left = sum(days[:month1-1]) + day1 
            right = sum(days_leap[month2:]) + days_leap[month2-1] - day2
            daysBt = daysBt - left - right 
        else:
            left = sum(days[:month1-1]) + day1 
            right = sum(days[month2:]) + days[month2-1] - day2
            daysBt = daysBt - left - right 
            

    return daysBt
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((2011,1,1,2012,12,31), 730),
                  ((1900,1,1,1999,12,31), 36523)
                  ]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
