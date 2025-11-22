import calender_display 
import calender_utils   
def main():
    """
    The main execution function. Handles user input, validation, and orchestration.
    """
    print("=== Modular Command-Line Calendar Generator ===")

    try:
        # get input from user
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (e.g., 2025): "))

        
        if 1 <= month <= 12 and year > 0:
            
            calender_display.print_calendar(month, year)
        else:
            print("Error: Month must be between 1 and 12, and Year must be a positive integer.")

    except ValueError:
        print("Error: Invalid input. Please enter valid integer numbers for month and year.")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    

    main()

