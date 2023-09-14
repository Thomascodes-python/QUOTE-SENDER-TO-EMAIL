import smtplib
from email.message import EmailMessage
import ssl
from motivational import quotes 
import random
import datetime 

#Getting the day
today = datetime.date.today()
today = today.strftime("%A")
print(today)
#

my_email = "emmanuelmenuwe078@gmail.com"
password = "YOUR-APP-PASSWORD"
receiver = "emmanuelmenuwe078@gmail.com"
 
body = f"HERE IS {today} MOTIVATIONAL QUOTE {random.choice(quotes)}"
 
email = EmailMessage()  

email["From"] = my_email
email["To"] = receiver
email.set_content(body)

content = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=content) as con:
    con.login(my_email,password)
    con.sendmail(my_email, receiver, email.as_string())
