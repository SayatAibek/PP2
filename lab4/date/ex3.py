from datetime import datetime
def microseconds():
    data=datetime.now()
    new_data=data.replace(microsecond=0)
    return data , new_data
print(microseconds())
    