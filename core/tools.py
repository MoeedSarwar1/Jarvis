from datetime import datetime


def get_time_date():
    date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    print(f"{date}")


get_time_date()
