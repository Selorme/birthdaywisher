import pandas
from datetime import datetime
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

PLACEHOLDER = "[NAME]"

# 1. Update the birthdays.csv
updated_birthdays = {
    "name": ["Becky", "Joy", "Mom", "Desmond", "Selorme"],
    "email": ["alekayuen51@gmail.com", "awalikahadome@gmail.com", "patiencemodzaka@gmail.com",
              "desmond.boateng@aims.ac.rw", "selormepythontest@gmail.com"],
    "year": [2000, 2000, 1978, 1998, 2000],
    "month": [8, 2, 6, 6, 6],
    "day": [9, 5, 26, 18, 21]
}

updated_birthdays_df = pandas.DataFrame(updated_birthdays)

updated_birthdays_df.to_csv("birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
month = today.month
day = today.day
csv_file = "birthdays.csv"
birthdays_df = pandas.read_csv(csv_file)

emails_to_send = []  # List to store email addresses of people with the same birthday

for index, row in birthdays_df.iterrows():
    birthday_month = row["month"]
    birthday_day = row["day"]

    if birthday_month == month and birthday_day == day:
        name = row["name"]
        email = row["email"]
        emails_to_send.append(email)  # Collect email addresses

        # 3. If step 2 is true, pick a random letter from letter templates and replace the
        # [NAME] with the person's actual name from birthdays.csv
        letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                            "letter_templates/letter_3.txt"]
        selected_letter_template = random.choice(letter_templates)

        with open(selected_letter_template, "r") as birthday_email_to_send:
            birthday_email = birthday_email_to_send.read()
            birthday_email_with_name = birthday_email.replace(PLACEHOLDER, name)

# 4. Send the letter generated in step 3 to all people sharing the same birthday.
my_email = os.environ["MY_EMAIL"]
password = os.environ["PASSWORD"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    for recipient_email in emails_to_send:
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                            msg=f"Subject: It's Your Birthday!\n\n{birthday_email_with_name}")
