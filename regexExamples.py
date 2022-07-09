
print("====with normal method====")
def isPhoneNumber(phone):
    if len(phone) != 12:
        return False 
    for i in range(0,3):
        if not phone[i].isdecimal():
            return False 
    if phone[3] != '-':
        return False
    for i in range(4,7):
        if not phone[i].isdecimal():
            return False 
    if phone[7] != '-':
        return False
    for i in range(8,12):
        if not phone[i].isdecimal():
            return False 
    return True

msg="Call me on 111-222-1234 in office, otherwise on my personal 222-333-1234."
foundNumber= False
for i in range(len(msg)):
    sub = msg[i:i+12]
    if isPhoneNumber(sub):
        print("Found number : " + sub)
        foundNumber = True

if not foundNumber:
    print("Number not found!")


import re

print("====with regex code====")
isPhone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = isPhone.findall(msg)
print(mo)

print("====with regex grouping====")
isPhone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = isPhone.search("Call me at 111-222-1234")
print("Phone Number : " + mo.group())
print("Area code : " + mo.group(1))

isPhone = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)')
mo = isPhone.search("Call me at (111) 222-1234")
print("Phone Number : " + mo.group())

print("====with regex non-greedy (zero or noe time)====")
isPhone = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = isPhone.search("Call me at 222-1234")
print(mo.group())

print("====with regex greedy (zero or more)====")
isPhone = re.compile(r'Bat(wo)*man')
print(isPhone.search("Batman"))


print("====with regex greedy (zero or more)====")
isPhone = re.compile(r'Bat(wo)+man')
print(isPhone.search("Batman"))
print(isPhone.search("Batwoman"))


print("====with regex piping====")
isPhone = re.compile(r'Bat(bat|mobile|man)')
mo = isPhone.search("I am Batman")
print(mo.group())


print("====with regex exact match====")
isPhone = re.compile(r'(Ha){3}')
print(isPhone.search("He said HaHaHa"))


print("====more regex greedy and nongreedy====")
isDigit = re.compile(r'(\d){3,5}')
print(isDigit.search("1234567890"))
isDigit = re.compile(r'(\d){3,5}?')
print(isDigit.search("1234567890"))
serve = "<server the diner> on the table."
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))


print("====with findall regex====")
isPhone = re.compile(r'\d+\s\w+')
msg = """12 drummers drumming
11 pipers piping
9 lords a leaping
9 ladies dancing
8 maids a milking
3 French hens"""
print(isPhone.findall(msg))


print("====dot caret dollar====")
isDigit = re.compile(r'^\d+$')
print(isDigit.findall("1234567890"))
isDigit = re.compile(r'First Name: (.*) Last Name: (.*)')
print(isDigit.findall("First Name: Batman Last Name: Robin"))
isDigit = re.compile(r'.at')
print(". means averything except new line")
print(isDigit.findall("cat wearing hat on a flat sitting on mat."))



print("====sub method====")
isName = re.compile(r'Agent \w+')
msg = 'Agent Alice gave secret doc to Agent Bob.'
print(isName.findall(msg))
print(isName.sub('REDACTED', msg))
isName = re.compile('Agent (\w)\w*')
print(isName.findall(msg))
print(isName.sub(r'Agent \1***', msg))



print("====verbose (for complex regex to format) -- check regex in code====")
isName = re.compile(r'''
(\d\d\d-) |      # area code w/o parens
(\(\d\d\d\))    # area code w parens and no dash
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last four digits
\sx\d{2,4}      # extension like x1234
''', re.VERBOSE | re.IGNORECASE)
