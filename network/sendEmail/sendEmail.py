# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os.path

# List of files:
# from.txt 	- contains 20 emails that will be used to send email, each line contains email and pass, separated by space							
# to.txt 		- contains emails to be sent, each email in one line
# body.txt	- contains body content of the email in HTML form

# Tasks: 
# 	- get each email from from.txt, send to 500 emails get from to.txt
# 	- get next email from from.txt, send to 500 different emails from to.txt
# 	- continue this process until no more email in to.txt to send

# Get all TO emails and store them in a list
if os.path.isfile('to.txt'):
	toEmails = open('to.txt').readlines()
	toEmails = [email.strip() for email in toEmails]
else:
	print "to.txt does not exist"

# Get all FROM emails and store them in a list
if os.path.isfile('from.txt'):
	fromEmails = open('from.txt').readlines()
else:
	print "from.txt does not exist"

# Get content of the email body
if os.path.isfile('body.txt'):
	emailBody = "\n".join(open('body.txt').readlines())
else:
	print "body.txt does not exist"

# This variable stores number of TO email to send
NUMBER_OF_EMAILS = 500

# Set the email body content to be sent as HTML 
body = MIMEText(emailBody, 'html')

email = MIMEMultipart()
email.attach(body)		

try:
	# Continue to send email when there is no email left in either FROM or TO email list
	while len(toEmails) or len(fromEmails):
		if len(fromEmails):
			sender = fromEmails[0]
		else:
			print "No more sender email!"
			break

		# If number of emails left is less than number of email need to be sent
		if len(toEmails):
			if len(toEmails) < NUMBER_OF_EMAILS:
				receivers = toEmails
			else:
				receivers = toEmails[:NUMBER_OF_EMAILS]			
		else:
			print "No more receiver email!"
			break

		# Extract usename and password of sender, used to login to Gmail
		senderUser = sender.split(' ')[0].strip()
		senderPass = sender.split(' ')[1].strip()

		email["Subject"] = "Mời tham gia khóa học lập trình Python"
		email["From"] = senderUser		
		email["To"] = ", ".join(receivers)

		# Login to Gmail and send emails using above senders and receivers
		serverSSL = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		serverSSL.ehlo()

		serverSSL.login(senderUser, senderPass)

		# SSL does not support TLS, no need to call serverSSL.starttls()
		serverSSL.sendmail(senderUser, receivers, email.as_string())
		serverSSL.close()

		print "Successful sending emails from %s to all receivers!" % (senderUser)

		# Remove emails already used to send or receive
		fromEmails = fromEmails[1:]
		toEmails = toEmails[NUMBER_OF_EMAILS:]		
		sleep(5000)
except:
	print "Unable to send email"
