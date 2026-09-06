# import  smtplib

# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#
#     #secure connection
#     connection.starttls()
#     #login
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="gmail.con",
#                         msg="Subject: Hello\n\nHello from Python!"
#                         )

#datetime library
import datetime as dt
#datetime class
now_time=dt.datetime.now()
year=now_time.year
month = now_time.month
weekday = now_time.weekday()
print(now_time)
print(year)
print(weekday)

date_of_birth = dt.datetime(year=2004,month=3,day=18)
print(date_of_birth)

