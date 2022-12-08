def alarm_clock(on_vacation, day):
    """Returns the alarm time, based on whether we are on vacation, and on what day it is."""
    if on_vacation:
        if 4 < day < 7:
            print("Your alarm has been turned off.")
        elif -1 < day < 5:
            print("Your alarm has been set to 10:00.")
    else:
        if 4 < day < 7:
            print("Your alarm has been set to 10:00.")
        elif -1 < day < 5:
            print("Your alarm has been set to 07:00.")

while True: 
    x = input("Are you on vacation?: ")
    if x == "yes":
        y = input("What day is it?: ")
        if y == "monday" or y == "tuesday" or y == "wednesday" or y == "thursday" or y == "friday":
            alarm_clock(True, 2)
        elif y == "saturday" or y == "sunday":
            alarm_clock(True, 6)
    elif x == "no":
        y = input("What day is it?: ")
        if y == "monday" or y == "tuesday" or y == "wednesday" or y == "thursday" or y == "friday":
            alarm_clock(False, 2)
        elif y == "saturday" or y == "sunday":
            alarm_clock(False, 6)
    else:
        break