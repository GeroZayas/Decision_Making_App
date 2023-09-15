from datetime import datetime, date, time, timedelta

# Get the current date and time
now = datetime.now()
print("Current date and time:", now)



# Get the current time
current_time = datetime.now().time()
print("Current time:", current_time)

# Create a datetime object from a string
date_string = "2022-09-15"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
print("Date object:", date_object)

# Format a datetime object as a string
formatted_date = date_object.strftime("%m/%d/%Y")
print("Formatted date:", formatted_date)

# Add or subtract time from a datetime object
one_day = timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day
print("Yesterday:", yesterday)
print("Tomorrow:", tomorrow)
