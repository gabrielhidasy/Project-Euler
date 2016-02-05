# It would probably be possible to just discover how many weeks there are/year

import calendar
cal = calendar.Calendar()
counter = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        cal_iter = cal.itermonthdays2(year, month)
        for day in cal_iter:
            if day[0] == 1 and day[1] == 6:
                counter += 1
print(counter)
