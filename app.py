"""
app.py

Script to write a timestamped message to a file and say hi.
"""

import os
from datetime import datetime

# Please customize the following variables
USER_NAME = "apoorvagupta"
VERSION = "1.0.0"

def say_hi(msg:str = "Hi!", file_directory:str = "/app/data/") -> None:
    """Timestamped say hi file"""
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    os.makedirs(file_directory, exist_ok=True)

    # Define filename with timestamp
    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)

    # Write the timestamp inside the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

def add_numbers(a:int, b:int) -> int:
    """Return the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    say_hi()
