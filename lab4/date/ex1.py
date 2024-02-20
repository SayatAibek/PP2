import datetime
def five_days():
    x=datetime.datetime.now()
    x=x+datetime.timedelta(-5)
    return x.strftime("%A")

print(five_days())
