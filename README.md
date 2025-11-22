# Modular Command-Line Calendar Generator
## Project Overview

This project is a lightweight, modular Python application designed to generate and display a formatted Gregorian calendar for any given month and year directly in the command-line interface (CLI). It serves as an exercise in implementing fundamental date arithmetic algorithms, specifically Zeller's Congruence, without relying on external date and time libraries (datetime, calendar).

The structure has been organized into three separate modules (files) to ensure high cohesion and low coupling, adhering to the project's modularity requirements (minimum three major functional modules).

## Features

Accurate Date Calculation: Correctly calculates the day of the week for the first day of any month using Zeller's Congruence.

Leap Year Handling: Includes logic to accurately determine leap years (divisible by 4, but not by 100 unless also by 400).

Modular Architecture: Project is split into dedicated modules for Logic, Presentation, and Control (main.py, calendar_utils.py, calendar_display.py).

ISO 8601 Compliance: Displays the calendar week starting on Monday (Mo).

Input Validation: Handles non-numeric and out-of-range inputs gracefully.

## Technologies/Tools Used

Primary Language: Python 3 (Standard Library Only)

Algorithm: Zeller's Congruence

## Architecture: Modular (Separation of Concerns)

Version Control: Git

Repository Host: GitHub

## Project Structure (Modules)

The project is divided into three distinct modules to meet the modularity requirement:

Steps to Install & Run the Project

Since this project uses only the standard Python library, no installation is required.

Save all three files (main.py, calendar_display.py, calendar_utils.py) into the same directory.

git clone [https://github.com/YourUsername/modular-calendar-generator.git](https://github.com/YourUsername/modular-calendar-generator.git)
cd modular-calendar-generator


Run the Main Script: (Always run the main.py file to start the application)

python main.py


Follow Prompts: The application will prompt you to enter the month (1-12) and the year (e.g., 2025).

## Instructions for Testing

Manual testing should be performed to verify functional requirements, particularly the accuracy of date calculations.

Critical Test Cases:

Leap Year Validation: Input Month 2, Year 2024 (Expected: 29 days).

Century Exception: Input Month 2, Year 1900 (Expected: 28 days, as 1900 is not divisible by 400).

Start Day Check: Input Month 12, Year 2024 (Expected: December 1st, 2024 is a Sunday, so the calendar starts on the last position of the first row).

Error Handling: Input 13 for the month (Expected: Error message).
