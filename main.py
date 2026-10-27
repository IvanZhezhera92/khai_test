from datetime import datetime
from pathlib import Path
from time import sleep

# Системний файл температури процесора Raspberry Pi.
sensor = Path("/sys/class/thermal/thermal_zone0/temp")

# Інтервал між вимірюваннями, с.
interval = 2

try:
    while True:
        # Перетворення тисячних часток градуса на градуси Цельсія.
        temperature = int(sensor.read_text()) / 1000
        timestamp = datetime.now().isoformat(timespec="seconds")

        # Виведення результату вимірювання в термінал.
        print(f"{timestamp} | Температура: {temperature:.1f} °C")

        # Додавання запису до CSV зі збереженням попередніх даних.
        with open("measurements.csv", "a", encoding="utf-8") as file:
            file.write(f"{timestamp},{temperature:.1f}\n")

        # Часова затримка між вимірюваннями.
        sleep(interval)

except KeyboardInterrupt:
    # Завершення виконання після натискання Ctrl+C.
    print("\nПрограму зупинено.")
