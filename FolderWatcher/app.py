import time

# simple method to output a message
def printMessage():
    print("This line will be printed.")

# Time execute to run and print the message at every interval
while True:           
    time.sleep(1)
    printMessage()