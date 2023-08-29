import time

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            break
        time.sleep(1)

# Get input from the user
alarm_time = input("Set the alarm time (HH:MM:SS): ")

# Set the alarm
set_alarm(alarm_time)
