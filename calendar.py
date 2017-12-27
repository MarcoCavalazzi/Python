"""
CALENDAR
Basic calendar the user can interact with from the command line. The user can choose to:
- View the calendar
- Add an event to the calendar
- Update an existing event
- Delete an existing event

It allows the user to insert events only in this or the following years.
"""

from time import sleep, strftime, gmtime

NAME = raw_input("Your name: ")
calendar= {}

def welcome():
  print "Welcome "+NAME+"!"
  sleep(1)
  print strftime("%A %m %d, %Y", gmtime())
  print strftime("%H:%M:%S", gmtime())
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar['date'] = update
      print "Update successful"
      print calendar
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      print "year %s"%date[6:10]
      print "strftime year %s"%strftime("%Y")
      if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")):
        print "Invalid year"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event added"
        print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "calendar empty"
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event deleted"
            print calendar
        else:
          print "An incorrect event was specified."
    elif user_choice == 'X':
      start = False
    else:
      print "An invalid command was entered."
      return

start_calendar()