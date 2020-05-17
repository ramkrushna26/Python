#! /bin/python3

#
# Ramkrushna Bolewar
#
# This script extract all phone numbers and emails from provided input file
#

import re, pyperclip

# create regex for phone number
phoneRegex = re.compile(r'''
# 111-222-1234, 111-1234, (111) 111-1234, 111-1234 ext 1234, ext. 1234, x1234
(
((\d\d\d) | (\(\d\d\d\)))?     # area code
(\s|-)                         # first seperator
\d\d\d                         # first 3 digits
-                              # 2nd seperator
\d\d\d\d                       # last 4 digits
((ext(\.)?\s|x)                # extension word part
(\d{2,5}))?                    # extention number part
)
''', re.VERBOSE)

# create regex for email address
emailRegex = re.compile(r'''
# some.+thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+                # name part
@                              # @ symbol
[a-zA-Z0-9_.+]+                # domain name part
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# Retrieve phone and email address
retrivedPhone = phoneRegex(text)
retrivedEmail = emailRegex(text)

phoneNumbers = []
for phone in retrievedPhone:
    phoneNumbers.append(phone[0])

# copy retrived phone and email to clipboard
results = '\n'.join(phoneNumbers) + '\n' + '\n'.join(retrievedEmail)
pyperclip.copy(results)
