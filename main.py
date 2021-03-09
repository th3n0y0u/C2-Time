import time
#Function: time()
print("Seconds since epoch = " + str(time.time()))

countdown = 3
while(countdown >= 0):
  print(countdown)
  countdown -= 1
  time.sleep(1)
print("VROOOOOOOOOOOOOOOOOOOOM!")

startTime = time.time()
userName = input("Type your name: ")
endTime = time.time()

print("Time: " + str(endTime - startTime))