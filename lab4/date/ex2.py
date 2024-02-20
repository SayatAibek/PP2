import datetime
def print_three_days():
    today=datetime.datetime.now()
    yesterday=today+datetime.timedelta(-1)
    tomorrow=today+datetime.timedelta(1)
    return yesterday.strftime("%A") , today.strftime("%A") , tomorrow.strftime("%A")
print(print_three_days())