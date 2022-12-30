import schedule
import time


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
print(t)

import smtplib


def job(ll):
    sender_email = "hawnscott171@gmail.com"

    rec_email = "7089406109@tmomail.net"

    password="cmjwicntwahghhjy"
    
  
    #ll = "You deserve nothing less than perfect from me, and that's what I'm striving for"

    msg = f"""Subject: I love you\n
{ll}
"""

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, password)

    print("Login success")

    server.sendmail(sender_email, rec_email, msg)

    print("Email has been sent to ", rec_email)

#sendNoto()

"""def job(ll):
    print("I'm working..."+ll)"""

schedule.every(1).minutes.do(job, "minutes")
schedule.every().hour.do(job, "hours")
schedule.every().day.at("21:55").do(job, "at time")

while 1:
    schedule.run_pending()
    time.sleep(1)
