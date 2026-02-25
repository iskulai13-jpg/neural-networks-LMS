import pandas as pd
from datetime import datetime

FILE = "datasets/attendance.xlsx"

def mark_attendance(name):
    time = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%Y-%m-%d")

    try:
        df = pd.read_excel(FILE)
    except:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    new_row = {"Name": name, "Date": date, "Time": time}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(FILE, index=False)

    print(f"{name} marked present")

if __name__ == "__main__":
    mark_attendance("Test Student")
