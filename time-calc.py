"""
calendar_arithmetic.py

A small toolkit of calendar/date arithmetic functions:
- days between two dates
- adding/subtracting days
- adding/subtracting months (calendar-aware)
- leap year check
- day-of-week lookup
- business days (weekdays only) between two dates
- age calculator
"""

import calendar
from datetime import date, timedelta


def days_between(date1: date, date2: date) -> int:
    """Return the number of days between date1 and date2 (can be negative)."""
    return (date2 - date1).days


def add_days(start: date, num_days: int) -> date:
    """Return the date that is num_days after (or before, if negative) start."""
    return start + timedelta(days=num_days)


def add_months(start: date, num_months: int) -> date:
    """Return the date that is num_months after (or before) start, clamping
    the day to the last valid day of the target month if needed."""
    month_index = start.month - 1 + num_months
    year = start.year + month_index // 12
    month = month_index % 12 + 1
    last_day_of_month = calendar.monthrange(year, month)[1]
    day = min(start.day, last_day_of_month)
    return date(year, month, day)


def is_leap_year(year: int) -> bool:
    """Return True if the given year is a leap year."""
    return calendar.isleap(year)


def day_of_week(d: date) -> str:
    """Return the full weekday name for a given date."""
    return calendar.day_name[d.weekday()]


def business_days_between(date1: date, date2: date) -> int:
    """Return the count of weekdays (Mon-Fri) strictly between date1 and date2."""
    if date1 > date2:
        date1, date2 = date2, date1
    total = 0
    current = date1 + timedelta(days=1)
    while current < date2:
        if current.weekday() < 5:
            total += 1
        current += timedelta(days=1)
    return total


def calculate_age(birthdate: date, on_date: date = None) -> int:
    """Return age in full years as of on_date (defaults to today)."""
    if on_date is None:
        on_date = date.today()
    years = on_date.year - birthdate.year
    had_birthday_this_year = (on_date.month, on_date.day) >= (birthdate.month, birthdate.day)
    if not had_birthday_this_year:
        years -= 1
    return years


def main():
    today = date.today()
    birthday = date(1995, 7, 20)
    project_start = date(2026, 1, 15)

    print(f"Today's date: {today}")
    print(f"Day of week for {project_start}: {day_of_week(project_start)}")
    print(f"Is 2028 a leap year? {is_leap_year(2028)}")
    print(f"Days between {project_start} and today: {days_between(project_start, today)}")
    print(f"90 days after {project_start}: {add_days(project_start, 90)}")
    print(f"6 months after {project_start}: {add_months(project_start, 6)}")
    print(f"3 months before {project_start}: {add_months(project_start, -3)}")
    print(f"Business days between {project_start} and today: "
          f"{business_days_between(project_start, today)}")
    print(f"Age for someone born on {birthday}: {calculate_age(birthday)}")


if __name__ == "__main__":
    main()
