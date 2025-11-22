# Project Statement

## Problem Statement

In environments where external libraries or specialized date utilities may be unavailable or undesirable (e.g., embedded systems, lightweight utilities, or educational exercises focusing on core algorithms), there is a need for a reliable, self-contained method to generate basic calendar information. The problem is to implement a calendar generator from first principles, specifically focusing on accurately determining the starting day of any given month and year using mathematical congruence, while ensuring robust leap year handling.

## Scope of the Project

The scope of this project is limited to generating a standard, text-based, single-month calendar view for a user-specified month and year.

### In Scope:

Implementation of Zeller's Congruence.

Leap year calculation logic.

Displaying the calendar grid with ISO 8601 week start (Monday).

Basic command-line input validation.

### Out of Scope:

Graphical User Interface (GUI).

Persistence or storage of calendar data.

Multi-year or multi-month views.

Holiday or event scheduling.

## Target Users

The primary target users are:

Developers/Students: Individuals needing a clean, educational example of core date algorithms implemented in Python.

System Administrators: Users who require a quick, zero-dependency utility for date referencing in command-line environments.

## High-Level Features

Input mechanism for month (1-12) and year.

Core logic module for date calculation (Zeller's Congruence).

Output module for formatted calendar display.
