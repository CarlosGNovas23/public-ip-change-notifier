import os
import requests
import time
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# ######################################################################################################################### #
# This script checks the public IP address every 10 minutes and sends an email notification if it changes.
# It uses the ipinfo.io API to get the current IP address and sends an email using Gmail's SMTP server.
#
# Make sure to create a .env file containing your Gmail password:
# .env file should contain:
# PASSWORD=your_gmail_password
#
# Note: You need to enable "Less secure app access" in your Google account settings for this to work.
# It is recommended to run this script on a Raspberry Pi or a server that is always on to keep track of your IP address.
# ######################################################################################################################### #



# On first run, it saves the current IP address and sends it to the email.
ip = ""

while (True):
    load_dotenv()
    
    # Function to get the current public IP address from ipinfo.io
    def get_json_data():
        try:
            url = 'https://ipinfo.io/json'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print("Error al obtener la dirección IP:", e)
            return None
    
    # Get the current IP address
    data = get_json_data()

    # Check if the ip address has changed
    if (ip != data["ip"]):
        ip = data["ip"]
        emailSender = "----------@gmail.com"  # Replace with the sender email address
        password = os.getenv("PASSWORD")
        emailReciver = "----------@gmail.com"  # Replace with the reciver email address
        subject = "Su IP ha cambiado"
        body = "Su nueva IP es: {}".format(ip)

        # Create the email message
        em = EmailMessage()
        em["From"] = emailSender
        em["To"] = emailReciver
        em["Subject"] = subject
        em.set_content(body)

        # Set up the SMTP server and send the email
        context = ssl.create_default_context()

        # Use SMTP_SSL for secure connection
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
            smtp.login(emailSender, password)
            smtp.sendmail(emailSender, emailReciver, em.as_string())

    # Wait for 10 minutes before checking again
    time.sleep(600)
    
# Created by Carlos Gómez Novas