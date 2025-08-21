import re
from datetime import datetime, timedelta
import pytz

# Exercise 1: Email Validation with Regex
def validate_email(email):
    pattern = r'^[\w\.-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$'
    return re.match(pattern, email) is not None


# Exercise 2: Extract Dates from Text
def extract_dates(text):
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)


# Exercise 3: Time Until Next Birthday
def time_until_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    current_year = now.year
    next_birthday = datetime(current_year, birthdate.month, birthdate.day)
    if next_birthday < now:
        next_birthday = datetime(current_year + 1, birthdate.month, birthdate.day)
    delta = next_birthday - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return days, hours, minutes


# Exercise 4: Timezone Converter
def convert_timezone(time_str, from_tz, to_tz):
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    dt = from_zone.localize(dt)
    return dt.astimezone(to_zone).strftime("%Y-%m-%d %H:%M:%S")


# Exercise 5: Log Timestamp Extraction
def parse_log_timestamps(log):
    pattern = r'\[(\d{2})/([A-Za-z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) \+\d{4}\]'
    months = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    matches = re.findall(pattern, log)
    results = []
    for day, mon, year, hour, minute, second in matches:
        month = months[mon]
        dt = datetime(int(year), month, int(day), int(hour), int(minute), int(second), tzinfo=pytz.utc)
        results.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
    return results


# Example Usage

# Exercise 1
print("----------------------Exercise 1: Email Validation------------------------------")
print(validate_email("user@example.com"))
print(validate_email("bad-email@.com"))

# Exercise 2
print("----------------------Exercise 2: Extract Dates---------------------------------")
text = "Important dates: 21-08-2025, 01/09/2025, and 15-09-2026"
print(extract_dates(text))

# Exercise 3
print("----------------------Exercise 3: Time Until Next Birthday----------------------")
birthdate = "2000-08-21"
print(time_until_birthday(birthdate))

# Exercise 4
print("----------------------Exercise 4: Timezone Converter----------------------------")
print(convert_timezone("2023-10-05 14:30:00", "US/Eastern", "UTC"))

# Exercise 5
print("----------------------Exercise 5: Log Timestamp Extraction----------------------")
log_data = '192.168.1.1 - - [21/Aug/2025:16:45:12 +0000] "GET /indx.html HTTP/1.1" 200 1024'
print(parse_log_timestamps(log_data))
