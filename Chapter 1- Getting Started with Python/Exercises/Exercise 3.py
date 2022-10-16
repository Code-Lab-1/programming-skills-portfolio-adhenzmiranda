#exercise 3
from datetime import datetime
now = datetime.now()
print (now)
dt_string = now.strftime("%d/%m/%y %H:%M:%S")
print(dt_string)