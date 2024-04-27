import pywhatkit
from datetime import datetime

# PyWhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features

PHONE_NUM = input('Enter your Phone Number: ') 
# Phone Number Must be a String with Country Code Like +91, +82

MESSAGE = input('Enter Message: ')
# Custom Message in string 

HR = int(input('Enter Hours: '))
# Hours in 24 Hour Format

MIN = int(input('Enter Minutes: '))
# Minutes 0-59

pywhatkit.sendwhatmsg(PHONE_NUM, MESSAGE, HR, MIN)
# Send a WhatsApp Message to a Contact based on the time

pywhatkit.sendwhatmsg(PHONE_NUM, MESSAGE, HR, MIN, True, 2)
# Same as above but Closes the Tab in 2 Seconds after Sending the Message

pywhatkit.sendwhatmsg_instantly(PHONE_NUM, MESSAGE, tab_close=False)
# Send WhatsApp Message Instantly (If Tab Close is True, the tab will be close Otherwise Not)

pywhatkit.image_to_ascii_art("c:\Images\hhh.jpg")
# This is used to convert an Image to an ASCII Art form that is stored in a text file.
# American Standard Code for Information Interchange

pywhatkit.playonyt(MESSAGE)
# opens the YouTube in your default browser and plays the video you mentioned in the function
# If you pass the topic name as parameter, it plays the random video on that topic. 
# On passing the URL of the video as the parameter, it open that exact video.