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
