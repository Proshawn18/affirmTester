import smtplib


def sendNoto():
    sender_email = "hawnscott171@gmail.com"

    rec_email = "7089406109@tmomail.net"

    password="cmjwicntwahghhjy"
    
  
    ll = "You deserve nothing less than perfect from me, and that's what I'm striving for"

    msg = f"""Subject: I love you\n
{ll}
"""

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, password)

    print("Login success")

    server.sendmail(sender_email, rec_email, msg)

    print("Email has been sent to ", rec_email)

sendNoto()
