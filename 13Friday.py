import datetime
from datetime import datetime
import calendar

def has_13friday(month, year):
    date = f'{month} 13 {year}'.format()
    check = datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[check]) == "Friday"

print(has_13friday(3,2020))