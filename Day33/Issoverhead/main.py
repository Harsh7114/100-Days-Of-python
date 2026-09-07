import requests
from datetime import datetime,time
import smtplib
import  time

MY_LAT = 12.900255# Your latitude
MY_LONG = 77.519087 # Your longitude
while True:

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # ---------------- CHECK CONDITIONS ---------------- #

    iss_is_near = (
            MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
            and
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )

    is_night = time_now >= sunset or time_now <= sunrise

    if iss_is_near and is_night:
        connection = smtplib.SMTP("smtp.gmail.com", 587)

        my_email = "your_email@gmail.com"
        password = "your_app_password"

        connection.starttls()
        connection.login(my_email, password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="recipient@gmail.com",
            msg="Subject: ISS Alert\n\nLook up! The ISS is above you."
        )

        connection.close()

    time.sleep(60)




    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.



