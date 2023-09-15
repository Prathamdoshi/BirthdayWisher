# BirthdayWisher

BirthdayWisher is a Python script that automates the process of sending birthday wishes to your friends and family via email. This script reads a list of people's birthdays from a CSV file, compares them with the current date, and if there's a match, it sends out a personalized birthday email from your account using the `smtplib` library. I deployed this script on PythonAnywhere for easy, hassle-free daily birthday wishes.

## How It Works

1. **CSV Input**: You provide a CSV file (`birthdays.csv`) that contains the names, email addresses, and birthdates of the people you want to send birthday wishes to. The CSV format should look like this:

Name,Email,Birthday
John Doe,johndoe@example.com,1990-09-14
Jane Smith,janesmith@example.com,1985-07-25


2. **Script Execution**: The script is scheduled to run daily, ideally using a task scheduler like `cron` or by setting up a scheduled task on platforms like PythonAnywhere.

3. **Matching Birthdays**: The script compares the birthdates in the CSV file with the current date using the `datetime` module. If today's date matches any of the birthdates, it proceeds to send out birthday wishes.

4. **Sending Birthday Emails**: The `smtplib` library is used to send emails from your account. It connects to your email server, logs in using your credentials, and sends a personalized birthday email to the recipients. Be sure to configure the script with your email server details and credentials.

5. **Personalized Messages**: You can customize the birthday message by modifying the `birthday_message` variable in the script to make it as personal and heartfelt as you want.

## Setting Up

1. Clone this repository to your local machine or the server where you plan to run the script.

git clone https://github.com/yourusername/BirthdayWisher.git


2. Create a CSV file named `birthdays.csv` in the project directory and add the details of the people you want to send birthday wishes to.

3. Configure the script with your email server details and credentials by modifying the following variables in the script:

- `SMTP_SERVER`: Your email server's SMTP address.
- `SMTP_PORT`: The SMTP port (usually 587 or 465).
- `EMAIL_ADDRESS`: Your email address (the one from which you want to send birthday wishes).
- `EMAIL_PASSWORD`: Your email password.
- `birthday_message`: Customize the birthday message to your liking.

4. Schedule the script to run daily using a task scheduler or platform-specific scheduling options.

5. Run the script manually at least once to ensure everything is set up correctly.

## Experience and Notes

I developed BirthdayWisher as a fun and thoughtful way to automate the process of sending birthday wishes to my friends and family. Here are some notes from my experience working on this project:

- Using the `datetime` module made it straightforward to compare dates and determine if a birthday falls on the current date.

- The `smtplib` library allowed me to send emails programmatically, and I took care to securely store my email credentials.

- PythonAnywhere provided a reliable platform for deploying and running the script daily without the need for constant server management.

Feel free to fork this project and adapt it to your needs. Have fun sending birthday wishes automatically!

**Note:** Make sure to keep your email credentials and personal information secure. It's a good practice to use environment variables or other secure methods to store sensitive information.
