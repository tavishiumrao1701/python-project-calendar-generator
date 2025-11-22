MONTHS = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """
    Checks if a given year is a leap year.
    Returns True if the year is divisible by 400, or divisible by 4 but not 100.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def get_days_in_month(month, year):
    """
    Returns the number of days in the specified month, adjusting for leap years.
    """
    # Check for February in a leap year
    if month == 2 and is_leap(year):
        return 29
    # Return days for other months
    return DAYS_IN_MONTH[month]

def get_start_day(month, year):
    """
    Calculates the day of the week (0=Mon, 6=Sun) for the 1st day of the month
    using Zeller's Congruence formula.
    """
    m = month
    y = year

    # Adjust month (Jan=13, Feb=14) and year for Zeller's formula
    if m < 3:
        m += 12
        y -= 1

    q = 1  # Day of the month (1st)
    K = y % 100 # Year of the century
    J = y // 100 # Century

    # Zeller's Congruence: (0=Sat, 1=Sun, ..., 6=Fri)
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

    # Convert Zeller's result to ISO 8601 standard (Monday=0, Sunday=6)
    return (h + 5) % 7