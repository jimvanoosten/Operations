def is_leap_year(year):
    """Returns whether the given year is a leap year."""
    # TODO
    if year % 4 == 0 and year % 100 != 0:
        print("{0} is a leap year".format(year))

    elif year % 400 == 0 and year % 100 == 0:
        print("{0} is a leap year".format(year))

    else:
        print("{0} is not a leap year".format(year))


is_leap_year(2013)
