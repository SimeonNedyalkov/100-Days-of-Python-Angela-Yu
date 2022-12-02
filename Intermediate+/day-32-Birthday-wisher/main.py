import smtplib

import pandas
import random

with open("quotes.txt") as quote_file:
    all_quotes= quote_file.readlines()
    quote = random.choice(all_quotes)

import datetime as dt
now = dt.datetime.now()
week = now.weekday()

if week == 0:
    my_email = "simeonpythontest@gmail.com"
    password = "enurqldowafxqvhv"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="simeon.nedyalkovv@gmail.com",
            msg=f"Subject: Hello\n\n{quote}"
     )


