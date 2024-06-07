import time
time = time.strftime("%H:%M:%S")
# time=(input("Enter the time:"))
print(time)

if(time>="00:00:00" and time<="11:59:59"):
  print("Good Morning Sir!")
elif(time>="12:00:00" and time<="16:59:59"):
  print("Good Afternoon Sir!")
elif(time>="17:00:00" and time<="19:59:59"):
  print("Good Evening Sir!")
elif(time>="20:00:00" and time<="23:59:59"):
  print("Good Night Sir!")