#-------------------- MODULES --------------------#
import datetime as dt
import random
import smtplib
import csv

#-------------------- GLOBAL VARIABLES --------------------#
birthdays = {} # birthdays dict to collect all the birthday that are on the current day
counter = 0 # counter to add a unique identifier to each dicts entry

today = dt.datetime.now() # get today's date
today_month = today.month # fetch month out of today's date
today_day = today.day # fetch day out of today's date


my_email = "prathamtest50@gmail.com" # my email string
my_password = "udseqbqzbonvggzg" # my password


# read in the data object and only fetch out people with birthdays today.
with open('birthdays.csv') as fileObject:

    reader_obj = csv.DictReader(fileObject) # read in the whole csv object

    for row in reader_obj: # loop through each row

        # only fetch out users who have birthdays today
        if int(row["month"]) == today_month and int(row["day"]) == today_day:

            birthdays[counter] = row

            counter = counter + 1

def draft_letter():

    rand = random.randint(1,3) # generate random integer to randome txt path
    file_url = f"letter_templates/letter_{rand}.txt"

    with open(file_url,"r") as f:

        lines = f.read() # read in the draft

        return lines # return the draft

if len(birthdays) > 0: # dont process the email if there are no birthdays today

    for i in range(0,len(birthdays)): # loop through all the individuals that have birthday today

        message = draft_letter() # get the letter
        name = birthdays[i]["name"] # get the name
        to_email = birthdays[i]["email"] # get the email
        message = message.replace("[NAME]",name) # replace the name

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # establist connection

            connection.starttls() # secure the connection
            connection.login(user=my_email,password=my_password) # log in to the account

            # send email
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject: Happy Birthday\n\n{message}"
            )






