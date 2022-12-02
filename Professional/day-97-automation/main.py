import smtplib

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user='simeonpythontest@gmail.com', password='smvvaatoftliwbsz')
connection.sendmail(from_addr='simeonpythontest@gmail.com', to_addrs='simeonpythontest@gmail.com', msg='Biser, please raise my salary please')
