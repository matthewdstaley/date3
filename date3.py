import re
import datetime
import time
from datetime import timedelta

#enter the date in mm/dd/yy when RPR occurred, if possible.
date = input("Write in the RPR date as mm/dd/yy:  ")
rpr =  str(date)
today = datetime.datetime.today()
RPR_date = datetime.datetime.strptime(rpr, "%m/%d/%y")
sixtydays = RPR_date + datetime.timedelta(days=60)
days_until_60days = sixtydays - today + datetime.timedelta(days=1)

print("RPR DATE: ", RPR_date.month,'/',RPR_date.day,'/',RPR_date.year)
print("CMF DATE: ", sixtydays.month,'/', sixtydays.day,'/',sixtydays.year)
print("Days Left: ", days_until_60days)

print('\n', '\n')

print("Hello, \n", "\n",
      
      "Thank you for your patience. The following payment dispute has been approved for further review as of ",
      RPR_date.month,'/',RPR_date.day,'/',RPR_date.year,'.', '\n','\n',
     "PAYMENT INFO", '\n', '\n',
     "Your customer now has a period of sixty days to potential re-open this case. If your customer does not re-open this case it will be officially closed on ", sixtydays.month,'/', sixtydays.day,'/',sixtydays.year, '.',
     "Feel free to write back in at that time for confirmation.", '\n', '\n',
     "Let me know if you have any further questions, I am happy to assist you.")
