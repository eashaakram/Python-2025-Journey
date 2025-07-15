# import time

# # Get current hour using local time
# current_hour = time.localtime().tm_hour

# # Greeting logic based on hour
# if 5 <= current_hour < 12:
#     print("Good Morning, Eesha! ☀️ Rise and shine!")
# elif 12 <= current_hour < 17:
#     print("Good Afternoon, Eesha! 🌤️ Keep pushing through!")
# elif 17 <= current_hour < 21:
#     print("Good Evening, Eesha! 🌆 Hope you had a great day!")
# else:
#     print("It's late, Eesha. 🌙 Time to rest. Good night!")

import time
timestamp = time.strftime('%H:%M:%S')
print("Current time:",timestamp)
hour = int(time.strftime('%H'))
if(hour >= 5 and hour < 12):
    print("Good Morning")
elif(hour >=12 and hour <= 16):
    print("Good Afternoon")
elif(hour >=17 and hour <= 21):
    print("Good Evening")
else:
    print("Good Night")