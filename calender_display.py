from calender_utils import MONTHS, get_days_in_month, get_start_day

def print_calendar(month, year):
    """
    Generates and prints the formatted calendar grid for the given month and year.
    """
    try:
        num_days = get_days_in_month(month, year)
        start_day_index = get_start_day(month, year) # 0=Mon, 6=Sun
    except IndexError:
        print("Fatal Error: Invalid month index passed to display module.")
        return

    # Print Header
    print(f"\n      {MONTHS[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")
    print("--------------------")

    # Print leading spaces (indentation for the first day)
    print("   " * start_day_index, end="")

    day_counter = start_day_index # Tracks position in the current week (0-6)

    # Print days of the month
    for day in range(1, num_days + 1):
        # f"{day:2d}" ensures uniform width for single and double-digit days
        print(f"{day:2d}", end=" ")

        day_counter += 1

        # Check if the week is complete
        if day_counter % 7 == 0:
            print() # Start a new line
            day_counter = 0

    print("\n") # Final newline for spacing