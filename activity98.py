import time

text = "Typing speed game in Python"

print("Type this sentence exactly:")
print("\n>>>", text, "\n")

input("Press Enter when you are ready...")

start = time.time()
typed = input("\nStart typing:\n>>> ")
end = time.time()

time_taken = end - start  # seconds
words = len(text.split())
wpm = (words / time_taken) * 60

print("\n⏱ Time Taken:", round(time_taken, 2), "seconds")
print("⚡ Speed:", round(wpm, 2), "WPM")

if typed == text:
    print("✅ Perfect typing!")
else:
    print("❌ There were mistakes in your typing.")