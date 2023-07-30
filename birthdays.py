from datetime import datetime, timedelta, date
from collections import defaultdict


def get_birthdays_per_week(users: list):
    
    birthdays_this_week = defaultdict(list)
    current_datetime = date.today()
    plus_week = current_datetime + timedelta(weeks=1)

    for user in users:
        birthday = date.fromisoformat(user["birthday"])
        
        next_b_day = birthday.replace(year=current_datetime.year) #дата дня народження в поточному році
        if current_datetime <= next_b_day < plus_week:
            if next_b_day.weekday() in [5, 6]:
                next_b_day += timedelta(days=(7 - next_b_day.weekday()))
        
                     
            birthdays_this_week[next_b_day].append(user["name"])
            
    for k, v in birthdays_this_week.items():
        day = k.strftime('%A')
        names = ", ".join(v)   
        print(f'{day}: {names}')

