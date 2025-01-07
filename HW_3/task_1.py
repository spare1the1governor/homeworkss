from datetime import datetime
from pickle import format_version
from time import strftime

def time_until_new_year():
    now = datetime.now()
    format_d=now.strftime("%Y.%m.%d %H:%M")
    date_obj = datetime.strptime(format_d, "%Y.%m.%d %H:%M")
    date_string = "2026.01.01 00:00"
    date_object = datetime.strptime(date_string, "%Y.%m.%d %H:%M")
    left=date_object-date_obj
    days = left.days
    hours, remainder = divmod(left.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    result=f"До Нового года осталось дней: {days}, часов: {hours}, минут: {minutes}!"
    return result
print(time_until_new_year())



