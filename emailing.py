
import smtplib

print("==== sending mail ====")

con = smtplib.SMTP('smtp.gmail.com', 587)
print(type(con))

#connect to server
print(con.ehlo())

#enable TLS
print(con.starttls())

#start sending email
con.login('ramkrushna.bolewar1@gmail.com', '')

con.sendmail('ramkrushna.bolewar1@gmail.com', 'ramkrushna.bolewar1@gmail.com', 'subject: Test mail from PY..\n\n This is test mail!!')

con.quit()

print("==== checking mail ====")

import imapclient

con = imapclient.IMAPClient('imap.gmail.com', ssl=True)
con.login('username', 'pwd')
con.select_folder('INBOX', readonly = True)
uids = con.search(['SINCE 20-FEB-2020'])
rawmsg = con.fetch(uids[0], ['BODY[]', 'FLAGS'])

#to get all folders
con.list_folders()

#to delete mail
con.select_folder('INBOX', readonly = False)
con.delete_messages(uids[0])

import pyzmail

msg = pyzmail.PyzMessage.factory(rawmsg[uids[0]][b'BODY[]'])
msg.get_subject()
msg.get_addresses('to')
msg.get_addresses('from')
#to check email part, will return true
msg.text_part
msg.html_part

msg.text_part.get_payload().decode('UTF-8')

