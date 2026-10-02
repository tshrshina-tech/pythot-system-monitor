import shutil
import time
from datetime import datetime

import psutil

CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent = (used / total) * 100
    return percent, total, used, free

def show_status():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk_percent, disk_total, disk_used, disk_free = get_disk_usage()

    print("\n" + "=" * 50)
    print("PYTHON SYSTEM MONITOR")
    print("=" * 50)
    print("Time:        ", now)
    print(f"CPU Usage:    {cpu:.1f}%")
    print(f"Memory Usage: {memory.percent:.1f}%")
    print(f"Disk Usage:   {disk_percent:.1f}%")
    print(f"CPU Cores:    {psutil.cpu_count(logical=True)}")
    print(f"Total RAM:    {memory.total / (1024**3):.2f} GB")
    print(f"Free Disk:    {disk_free / (1024**3):.2f} GB")

    print("\nAlerts:")
    print("WARNING: CPU usage is high." if cpu >= CPU_LIMIT else "CPU usage is normal.")
    print("WARNING: Memory usage is high." if memory.percent >= MEMORY_LIMIT else "Memory usage is normal.")
    print("WARNING: Disk usage is high." if disk_percent >= DISK_LIMIT else "Disk usage is normal.")
    print("=" * 50)

def main():
    print("Starting Python System Monitor...")
    print("Press Ctrl+C to stop.")
    try:
        while True:
            show_status()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
