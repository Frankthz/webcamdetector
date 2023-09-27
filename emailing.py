import smtplib
import imghdr
from email.message import EmailMessage

SENDER = "USER"
PASSWORD = "PASSWORD"
RECEIVER = "RECEIVER"

def send_email(image_path):
    print("send_email started")
    email_message = EmailMessage()
    email_message["Subject"] = "Something showed up!"
    email_message.set_content("Hey, something is in there!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email ended")