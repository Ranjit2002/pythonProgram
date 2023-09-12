"""
# We can use else part with for and while loop means both loop

for i in range(5):  # Else part will execute after the execution of the loop is completed
    print(i)
else:
    print("Sorry! loop will not print 5")

for i in []:
    print(i)
else:
    print("list is empty")

for i in range(6):  # Here else part will not execute because the loop was broke in between
    print(i)
    if i == 4:
        break
else:
    print("Sorry!")

i = 0
while i < 5:    # Here I used else with while loop
    print(i)
    i += 1
else:
    print("Sorry!")
"""
# for x in range(5):
#     print("Iteration no {} in for loop".format(x+1))
# else:
#     print("else block in loop")
# print("Out")

# import time
#
# text = "Loading..."
# for char in text:
#     print(char, end='', flush=True)
#     time.sleep(0.5)  # Sleep for half a second
#     print('\b', end='', flush=True)  # Move the cursor back one position

import time

text = "Loading..."
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.5)  # Sleep for half a second
    print('\b', end='', flush=True)  # Move the cursor back one position
