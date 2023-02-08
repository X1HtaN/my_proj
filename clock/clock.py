from datetime import datetime

months = {"1" : "января",
"2" : "февраля",
"3" : "марта",
"4" : "апреля",
"5" : "мая",
"6" : "июня",
"7" : "июля",
"8" : "августа",
"9" : "сентября",
"10" : "октября",
"11" : "ноября",
"12" : "декабря"}

def check_month(month):
    month = str(month)
    for i in months.items():
        if i[0] == month:
            return i[1]

def current_time():
    current_time = datetime.now()
    day = str(current_time.day).rjust(2, "0")
    hours = str(current_time.hour).rjust(2, "0")
    minutes = str(current_time.minute).rjust(2, "0")
    seconds = str(current_time.second).rjust(2, "0")
    month = check_month(current_time.month)

    return f"сегодня {day} {month} {current_time.year}, {hours}:{minutes}:{seconds}"
