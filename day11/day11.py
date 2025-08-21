import re
from datetime import datetime
import pytz

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

emails = ["user@example.com", "bad-email@.com", "mohammad@ai.edu.jo"]
for e in emails:
    print(f"{e} -> {'Valid' if validate_email(e) else 'Invalid'}")

timezones = ["UTC", "Asia/Amman", "America/New_York"]

print("\nCurrent Times:")
for tz in timezones:
    zone = pytz.timezone(tz)
    now = datetime.now(zone)
    print(f"{tz}: {now.strftime('%Y-%m-%d %H:%M:%S')}")
import re
from datetime import datetime, timedelta
import pytz

data = [
    "Order 3 apples and 5 bananas on 21-08-2025, contact: user@example.com",
    "Order 10 oranges and 2 mangoes on 01-09-2025, contact: bad-email@.com",
    "Order 7 pears and 4 kiwis on 15-09-2025, contact: mohammad@ai.edu.jo"
]

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

for entry in data:
    numbers = re.findall(r'\d+', entry)
    print(f"\nFrom '{entry}'")
    print("Extracted numbers:", numbers)

    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w{2,}', entry)
    if email_match:
        email = email_match.group(0)
        print(f"Email: {email} -> {'Valid' if validate_email(email) else 'Invalid'}")

    date_match = re.search(r'(\d{2}-\d{2}-\d{4})', entry)
    if date_match:
        date_str = date_match.group(1)
        order_date = datetime.strptime(date_str, "%d-%m-%Y")

        utc = pytz.utc
        amman = pytz.timezone("Asia/Amman")
        ny = pytz.timezone("America/New_York")

        utc_time = utc.localize(order_date)
        amman_time = utc_time.astimezone(amman)
        ny_time = utc_time.astimezone(ny)

        print("Order Date:", date_str)
        print("UTC:", utc_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Amman:", amman_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("New York:", ny_time.strftime("%Y-%m-%d %H:%M:%S"))

        future_date = amman_time + timedelta(days=7)
        print("One week later (Amman):", future_date.strftime("%Y-%m-%d %H:%M:%S"))
        future_date_ny = ny_time + timedelta(days=7)
        print("One week later (New York):", future_date_ny.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print("No valid date found in the entry.")
    print("-" * 40) 