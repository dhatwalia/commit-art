# Date must start from Sunday for Github

import sys
from datetime import date, timedelta, datetime


def skip_week(date):
    return date + timedelta(days=7)


def first_sunday(year):
    # January 1st of the year
    first_sunday = date(year, 1, 1)
    # First Sunday of the year
    first_sunday += timedelta(days=6 - first_sunday.weekday())
    return first_sunday


def last_sunday(year):
    # December 31st of the year
    last_sunday = date(year, 12, 31)
    # Last Sunday of the year
    if last_sunday.weekday() == 6:
        return last_sunday
    else:
        last_sunday -= timedelta(days=last_sunday.weekday() + 1)
        return last_sunday


def write(output):
    file = open("dates.txt", "a")
    for date in output:
        file.write(str(date)+"\n")
    file.close()


def get_dates(message, date, weeks_available):
    output = []
    for char in message:
        if weeks_available <= 4:
            print("Not enough room to display message.")
            exit()
        if char == "A":
            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "B":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
        elif char == "C":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "D":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
        elif char == "E":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "F":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
        elif char == "G":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "H":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "I":
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "J":
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
        elif char == "K":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=6)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "L":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "M":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=6)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "N":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "O":
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
        elif char == "P":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
        elif char == "Q":
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=5)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "R":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "S":
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
        elif char == "T":
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
        elif char == "U":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
        elif char == "V":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
        elif char == "W":
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
        elif char == "X":
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
            output.append(date)

            date += timedelta(days=5)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=6)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        elif char == "Y":
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=8)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)

            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=5)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=7)
        elif char == "Z":
            output.append(date)
            date += timedelta(days=5)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            date += timedelta(days=3)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=2)
            output.append(date)
            date += timedelta(days=4)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=1)
            output.append(date)
            date += timedelta(days=5)
            output.append(date)
            weeks_available -= 1

            date += timedelta(days=1)
        date = skip_week(date)
        weeks_available -= 1

    return output, weeks_available


if __name__ == "__main__":
    year = sys.argv[1]
    if not year.isnumeric():
        print("The first argument should only contain number digits in YYYY format. Example: 2018.")
        exit()
    year = datetime.strptime(year, "%Y").year

    message = sys.argv[2]
    message = message.upper()
    if not message.isalpha():
        print("The second argument should only contain alphabets. Example: ABC")
        exit()

    first = first_sunday(year)
    last = last_sunday(year)
    weeks_available = ((last - first) / 7).days

    output, weeks_available = get_dates(message, first, weeks_available)
    write(output)
