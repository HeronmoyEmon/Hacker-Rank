def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year = int(input('>'))
print(is_leap(year))

'''
for year 1992 which is a leap year
it is evenly divisible by 4 but not by 100
again 1800 is not a leap year
evenly divisible by 100 but not by 400
century years are leap year
only if divided by 400'''


'''
first we check if century year. 
century year should be must divisible by 400.
if it's true, then leap year. condition- must be divisible by 400 
second, if not century year then it is not divisible by 100
check if divisible by 4, then it is leap year. condition - divisible by 4 but not 100
'''