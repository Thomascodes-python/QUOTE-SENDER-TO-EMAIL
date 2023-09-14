import smtplib
from email.message import EmailMessage
import ssl

my_email = "emmanuelmenuwe078@gmail.com"
password = "vsqhldhyrtaymurc"
receiver = "emmanuelmenuwe078@gmail.com"
 
body = "Hello world its time to hack"
 
email = EmailMessage()  

email["From"] = my_email
email["To"] = receiver
email.set_content(body)

content = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=content) as con:
    con.login(my_email,password)
    con.sendmail(my_email, receiver, email.as_string())