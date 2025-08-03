Yes, you can configure your **Raspberry Pi 4B** to **automatically shut down** (or reboot, or throttle) when it reaches a specific temperature like **70°C**, using a simple **background script** or **systemd service**.

---

### ✅ Method: Custom Python script with shutdown at 70°C

Here’s a basic script:

```python
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
```

---

### 🛡️ To run it safely:

1. **Make it executable:**

```bash
chmod +x shutdown_if_hot.py
```

2. **Run at boot using systemd:**

Create a service file:

```bash
sudo nano /etc/systemd/system/temp-monitor.service
```

Paste:

```ini
[Unit]
Description=Shutdown Raspberry Pi if temperature is too high
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/shutdown_if_hot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable it:

```bash
sudo systemctl daemon-reexec
sudo systemctl enable temp-monitor
sudo systemctl start temp-monitor
```

---

### 🧪 Notes:

* This script uses **`/sys/class/thermal/thermal_zone0/temp`**, which is available without extra packages.
* The script **shuts down at 70°C** — you can adjust the threshold.
* Make sure the script is stored in a reliable location (e.g., `/usr/local/bin/` or `/opt/`).

---

Let me know if you'd prefer a more passive approach (like sending a warning email or logging instead of shutting down).

