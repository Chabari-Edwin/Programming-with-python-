def add_time(start, duration, starting_day=None):
    # Days of the week in order
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Convert start hour to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate new minutes and hours
    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute %= 60
    
    end_hour = start_hour + duration_hour + extra_hour
    days_later = end_hour // 24
    end_hour %= 24
    
    # Convert end hour back to 12-hour format
    if end_hour >= 12:
        period = "PM"
        if end_hour > 12:
            end_hour -= 12
    else:
        period = "AM"
        if end_hour == 0:
            end_hour = 12

    # Calculate the final day of the week
    if starting_day:
        starting_day = starting_day.capitalize()
        day_index = (days_of_week.index(starting_day) + days_later) % 7
        final_day = days_of_week[day_index]
        day_part = f", {final_day}"
    else:
        day_part = ""

    # Determine days later string
    if days_later == 1:
        later_part = " (next day)"
    elif days_later > 1:
        later_part = f" ({days_later} days later)"
    else:
        later_part = ""
    
    # Format the new time
    new_time = f"{end_hour}:{end_minute:02d} {period}{day_part}{later_part}"
    
    return new_time

# Example usage:
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "Tuesday"))
print(add_time("6:30 PM", "205:12"))
