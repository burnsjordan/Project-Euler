count = 0
current_year = 1901
current_day = 1
current_month = 1
months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

while current_year <= 2000:
    while current_month <= 12:
        if(current_day % 7 == 1):
            count += 1
        if(current_year % 4 == 0 and current_month == 2):
            current_day += 29
        else:
            current_day += months[current_month]
        current_month += 1
    current_month = 1
    current_year += 1

print(count)