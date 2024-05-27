import re

def detect_date(s):
    date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    for day, month, year in date_regex.findall(s):
        day = int(day)
        month = int(month)
        year = int(year)
        if year < 1000 or year > 2999:
            print(f'不正な年です {year}')
            return None

        if month < 1 or month > 12:
            print(f'不正な月です {month}')
            return None

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                max_day = 29
            else:
                max_day = 28
        elif month in (4, 6, 9, 11):
            max_day = 30
        else:
            max_day = 31
        if day < 1 or day > max_day:
            print(f'不正な日です {day}')
            return None
        return day, month, year
    return None

date=input('入力して下さい:')

date_r=detect_date(date)

if date_r==None:
    print('入力ミスしています。')
else:
    print(f"{date_r[0]}/{date_r[1]}/{date_r[2]}")



# import re

# date=input('入力して下さい:')

# date_list=date.split()


# re.compile(r'^(0[1-9]|[12][0-9]|[3][01])/(0[1-9]|1[0-2])/[12][0-9]\d{3}$')

# # ^(0[1-9]|[12][0-9]|[3][01])/(0[1-9]|1[0-2])/[12][0-9]\d{3}$
# # ^(0[1-9]|[12][0-8])/(2)//[12][0-9]\d{3}$
# # ^(0[1-9]|[12][0-9]|30)/(0[1-9]|1[0-2])/[12][0-9]\d{3}$

# def date_2(date):
#     re.compile(r'^(0[1-9]|[12][0-8])/(2)//[12][0-9]\d{3}$')

# if date_list[1]=='2' and int(date_list[3])<2999 and 1000>int(date_list[3]):
#     date_2(date)