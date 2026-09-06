##################### Extra Hard Starting Project ######################
import smtplib
import  datetime as dt
import random
from email.message import EmailMessage
# 1. Update the birthdays.csv
with open(file="birthdays.csv",mode="r")as f:
    line = f.readlines()
#print(line)
# 2. Check if today matches a birthday in the birthdays.csv
today=dt.datetime.now()
today_month = today.month
today_day = today.day

for row in line[1:]:
    data = row.strip().split(",")
    if int(data[3]) == today_month and int(data[4]) == today_day:
        print("Birthday found!")
        # Person's details
        birthday_person_name = data[0]
        birthday_person_email = data[1]

        random_template = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(random_template,"r", encoding="utf-8") as letter_file:
            contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person_name)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "Your_gmail@gmail.com"
password = "Your gmail app password"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    # connection.sendmail(
    #     from_addr=my_email,
    #     to_addrs=birthday_person_email,
    #     msg=f"Subject:Happy Birthday!\n\n{contents}"
    # )
    msg = EmailMessage()
    msg["Subject"] = "Happy Birthday!"
    msg["From"] = my_email
    msg["To"] = birthday_person_email
    msg.set_content(contents, charset="utf-8")
    print(contents)
    connection.send_message(msg)


