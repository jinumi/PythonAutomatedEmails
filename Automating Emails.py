# Python code to send an email using SMTP protocol and Gmail account
# Importing necessary modules
import smtplib as s
from email.message import EmailMessage

# Creating an EmailMessage object
email = EmailMessage()

# Setting up the email parameters
email['from'] = 'xyz name' # Sender's name
email['to'] = 'xyz id' # Recipient's email address
email['subject'] = 'xyz subject' # Subject of email
email.set_content("Xyz content of email") # Content of email

# Creating an SMTP object and sending the email
with s.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # Greeting the server
    smtp.ehlo()
    # Establishing a secure connection with the server
    smtp.starttls()
    # Logging into the sender's Gmail account
    smtp.login("email_id", "Password")
    # Sending the email
    smtp.send_message(email)

# Printing success message
print("Email sent successfully!")