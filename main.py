##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import os
import datetime as dt
import pandas as pd
import random
import smtplib
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
today = dt.date.today()
print(today.month, today.day)
birth_dates = pd.read_csv('birthdays.csv')
birthdays = pd.DataFrame(birth_dates)
for i in range(birthdays.shape[0]):
    if birthdays["month"][i] == today.month and birthdays["day"][i] == today.day:
        random_letter = random.randint(1, 3)
        # 1. Read the file content
        with open(f"letter_templates/letter_{random_letter}.txt", "r") as file:
            file_contents = file.read()

        # 2. Replace the text in memory
        modified_contents = file_contents.replace("[NAME]", birthdays["name"][i])

        # 3. Write the modified content back to the file
        with open(f"letter_templates/letter_{random_letter}.txt", 'w') as file:
            file.write(modified_contents)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="mohamed.moneib.98@gmail.com",
                                msg=f"Subject:Happy Birthday!\n\n{modified_contents}")





