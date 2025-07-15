import time

# Get current hour using local time
current_hour = time.localtime().tm_hour

# Greeting logic based on hour
if 5 <= current_hour < 12:
    print("Good Morning, Eesha! ☀️ Rise and shine!")
elif 12 <= current_hour < 17:
    print("Good Afternoon, Eesha! 🌤️ Keep pushing through!")
elif 17 <= current_hour < 21:
    print("Good Evening, Eesha! 🌆 Hope you had a great day!")
else:
    print("It's late, Eesha. 🌙 Time to rest. Good night!")
