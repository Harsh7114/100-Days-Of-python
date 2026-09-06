import random
import smtplib
lines = []
with open(file="quotes.txt",mode="r") as f:
    #line = f.readline()
    for line in f:
        lines.append(line)
    #f.readlines return a list of lines so no need of for loop
#print(lines)
#using list comprehension
with open("quotes.txt", mode="r") as f:
    lines = [line.strip() for line in f]

quote = random.choice(lines)
my_email = "Your_gmail"
password = "Your gmail app password"
smtp = smtplib.SMTP("smtp.gmail.com",587)
smtp.starttls()
smtp.login(user=my_email,password=password)
smtp.sendmail(from_addr=my_email,to_addrs="harshranjan2582779@gmail.com",msg=f"Subject:Quote of the day\n\n{quote}")


print(quote)