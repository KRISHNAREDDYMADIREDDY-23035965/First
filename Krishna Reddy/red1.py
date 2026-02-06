from datetime import datetime

# Ask user for input
user_text = input("Enter a line of text: ")

# Get current timestamp
timestamp = datetime.now()

# Open file in append mode and write data
with open("log.txt", "a") as file:
    file.write(f"[{timestamp}] {user_text}\n")

print("Text successfully added to log.txt")
