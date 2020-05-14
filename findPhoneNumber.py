
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


print("====with findall regex====")
isPhone = re.compile(r'\d+\s\w+')
msg = """12 drummers drumming
11 pipers piping
9 lords a leaping
9 ladies dancing
8 maids a milking
3 French hens"""
print(isPhone.findall(msg))
