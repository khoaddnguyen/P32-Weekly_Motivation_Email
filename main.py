import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

SUBJECT = "Daily Motivation"
BODY = "This is the body"
SENDER_EMAIL = "mykoiva007@gmail.com"
RECIPIENT_EMAIL = ["santosgui102@yahoo.com"]
PASSWORD = "oddmqghemfakxcuo"  # security application password, not account password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:  # a week starts with Monday  = 0
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        BODY = random.choice(all_quotes)

    print(BODY)
    def send_email(SUBJECT, BODY, SENDER_EMAIL, RECIPIENT_EMAIL, PASSWORD):
        msg = MIMEText(BODY)
        msg["Subject"] = SUBJECT
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(RECIPIENT_EMAIL)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
           smtp_server.login(SENDER_EMAIL, PASSWORD)
           smtp_server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print("Message sent!")


    send_email(SUBJECT, BODY, SENDER_EMAIL, RECIPIENT_EMAIL, PASSWORD)

# subject = "Hello"
# body = "This is the body of the text message"
# sender = "mykoiva007@gmail.com"
# recipients = ["santosgui102@yahoo.com"]
# password = "oddmqghemfakxcuo"  # security application password, not account password
#
# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = sender
#     msg["To"] = ", ".join(recipients)
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")
#
#
# send_email(subject, body, sender, recipients, password)


