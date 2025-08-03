#!/usr/bin/env python3
import time
import os

# Threshold in Celsius
MAX_TEMP = 70

def get_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp_str = f.read().strip()
        return int(temp_str) / 1000  # Convert to Celsius

while True:
    temp = get_temp()
    print(f"Current temperature: {temp}°C")
    if temp >= MAX_TEMP:
        print("Temperature too high! Shutting down...")
        os.system("sudo shutdown now")
        break
    time.sleep(10)  # Check every 10 seconds

