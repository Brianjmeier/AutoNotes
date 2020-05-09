'''
Instructions:
The script will need your Google Keep email and password to work.
'''
email = ""
password = ""
'''
If you use Firefox set the variable below to 1, if you are a Chrome user set it to 2.
Then download the corresponding drivers:
Firefox: 'https://github.com/mozilla/geckodriver/releases'
Chrome: 'https://sites.google.com/a/chromium.org/chromedriver/downloads'
Installation Instructions: 'https://selenium-python.readthedocs.io/installation.html#drivers'

You will also need to install selenium and gkeepapi APIs.
'''
browser = 
'''
First of all you need to create a WhatsApp group to send notes to.
Set the following variable to the name of such group.
'''
group_name = ""
'''
Now you can send messages to that group with the following format:
    To create a new note: "Title - Text"
    ('space hyphen space' between the title and the text)
    To create a new list: "*ListTitle - item1, item2#, item3"
    (a star at the beginning of the title then 'space hyphen space' and the items between 'coma space'
    if you want an item to appear checked add # at the end like in 'item2')

Now you are ready to run the script!
Do so by opening the terminal on the AutoNotes folder and typing 'python autonotes.py'
Then WhatsApp Web will open in your browser of choice
and you'll have 7 seconds to scan the QR Code.
Then your notes and lists will be synced to your Google Keep account.
Note (no pun intended) that all massages will be deleted from you group.
Star massages that you want to keep (yes, I did it again),
but those will be copied to Keep every time you run the script.
'''
'''
Feel free to contact me at brianjonathanmeier at gmail.com for any comments or bug reports
'''
