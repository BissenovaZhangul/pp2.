#1
from datetime import datetime, timedelta
x=datetime.now()
y=x-timedelta (days=5)
print(x)
print(y)

#2
from datetime import datetime, timedelta
x=datetime.now()
y=x-timedelta (days=1)
z=x+timedelta (days=1)
print("Yesterday: ", y)
print("Today: ", x)
print("Tomorrow: ", z)

#3
from datetime import datetime
x=datetime.now()
y=x.replace(microsecond=0)
print(x)
print(y)

#4
from datetime import datetime
d1 = datetime(2021, 5, 15, 8, 30, 0)
d2 = datetime(2021, 5, 15, 9, 45, 30)
difference = (d2 - d1).total_seconds()
print("Time difference in seconds:", difference)