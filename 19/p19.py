import numpy as np

days_months_normal_year = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_months_leap_year = days_months_normal_year.copy()
days_months_leap_year[2] = 29

days_months_normal_year = np.cumsum(days_months_normal_year)
days_months_leap_year = np.cumsum(days_months_leap_year)

print(days_months_normal_year, days_months_leap_year)

count = 0
difference = 1
first_loop_done = False

for year in range(1900, 2001):
    max_days = 0
    days_months_cum = []

    if (year % 100 == 0 and year % 400 != 0) or year % 4 != 0:
        max_days = 365
        days_months_cum = days_months_normal_year
    else:
        max_days = 366
        days_months_cum = days_months_leap_year
    
    day = difference
    print(day)
    while day <= max_days:
        if day in days_months_cum and first_loop_done and year >= 1901:
            print(day, year)
            count += 1
        
        if first_loop_done:
            day += 7
        else:
            day += 6
        
        first_loop_done = True
    
    difference = day - max_days
    print(day, difference)

print(count)
