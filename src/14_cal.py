"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

def cal_function(sysArgs):

  if(len(sysArgs) == 1):
    # there are no params
    #  If the user doesn't specify any input, your program should
    #    print the calendar for the current month. The 'datetime'
    #    module may be helpful for this.
    # print(datetime.now().month)
    my_date = datetime.now()
    print(calendar.month(my_date.year, my_date.month))
    # print(datetime.now())

  elif(len(sysArgs) == 2):
    #  - If the user specifies one argument, assume they passed in a
    #    month and render the calendar for that month of the current year.
      my_date = datetime.now()
      # print(sysArgs[1])
      print(calendar.month(my_date.year, int(sysArgs[1])))
  elif(len(sysArgs) == 3):
    #  - If the user specifies two arguments, assume they passed in
    #    both the month and the year. Render the calendar for that
    #    month and year.
      month = int(sysArgs[1])
      year = int(sysArgs[2])
      print(calendar.month(year, month))
  else:
    # Do they want me to validate the inputs? If not, isn't this case the same as the first(no inputs)
  #  - Otherwise, print a usage statement to the terminal indicating
  #    the format that your program expects arguments to be given.
  #    Then exit the program.
      print('You need to specify a month or a year')
      exit()

  # [print(a) for a in sys.argv]

cal_function(sys.argv)