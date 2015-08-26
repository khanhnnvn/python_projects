This project contains following files:

1. sendEmail.py - source code
2. body.txt - contains email content
3. from.txt - contains all emails used to send, each line contains email and password, must be separated by a single space
4. to.txt - contains all emails used to receive email, each email in a separate line

Logic:

- Use stmplib library comes with Python
- Get each email address from from.txt one by one
- Get a number of email addresses from to.txt (500 as required but can be configured by NUMBER_OF_EMAILS in source code)
- If there is no email in from.txt (no sender) but there are still emails in to.txt, display "No more sender email"
- If there is no email in to.txt (no receiver) but there are still emails in from.txt, display "No more receiver email"
- Setup SMTP SSL server and login to Gmail by each sender got from from.txt
- Send the email to every senders got from to.txt by joining all receiver emails to a single string, separated by commas
- Print out result for each sender and all receivers after sending email
- Must set the MIMEText() mode to 'html' so the email body can display as HTML 

Note:
- The program still does not check if records in from.txt are separated by a single space, will update in future
