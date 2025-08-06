#!/usr/bin/env python3
import time
import os
import argparse

parser = argparse.ArgumentParser(description="Monitor CPU temperature and shut down if it exceeds a threshold.")
parser.add_argument("--max-temp", type=int, default=70, help="Maximum allowed temperature in Celsius before shutdown (default: 70)")
args = parser.parse_args()

MAX_TEMP = args.max_temp

print(f"Shutting down if temperature exceeds {MAX_TEMP}°C")

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

