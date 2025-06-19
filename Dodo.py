import datetime
import time

# Simulated database
event_list = []

# Function to simulate setting an event
def set_event(date, time_, message):
    event_list.append({'date': date, 'time': time_, 'message': message})

# Uncomment to simulate an event:
# set_event("2025-06-10", "17:00", "Meeting with Nidhi")

while True:
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")

    event_found = False

    for event in event_list:
        if event["date"] == current_date and event["time"] == current_time:
            print(f"Dodo says: {event['message']}")
            event_found = True
            time.sleep(60)  # Avoid repeating

    if not event_found:
        print(f"Current Time: {current_time} | Date: {current_date}")

    time.sleep(10)
