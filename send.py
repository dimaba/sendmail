"""This example shows all necessary steps for sending a basic plain text message."""

# Import the MailSender class from the sendmail module
from sendmail import MailSender

# First, let's create the plain text email we want to send. If you create this message manually in a Python script,
# you will have to specify newlines etc yourself. To avoid that you can write the message separately in a text file
# and then read it with your Python script.

plaintext = "Hello John, \n" \
            "I'm just testing my new fancypants email sending system here.\n" \
            "Adam"

# Next, we create the MailSender object which will handle connecting to the server, as well as composing and sending
# our email. For this, we need to enter the username, password and server address/port for a working SMTP server.
# If you have an email account with one of the major email providers (e.g. Gmail or equivalent) you can often find
# the SMTP server information online. You will also need to know which authorization type the SMTP server requires:
# SSL or TLS. The MailSender defaults to using TLS. See the Readme for more information.
# The settings used below illustrate connecting to Gmail's SMTP server using TLS.

ourmailsender = MailSender('username@gmail.com', 'password', ('smtp.gmail.com', 587))

# We can now set the body of the message. For this, we will use your previously created plain text message.
# We will also add a subject for our email and specify the name of the sender (the 'From' name). Both the subject
# and the sender's name can also be set individually later, or be left blank. Some servers only accept specific formats
# for the sender's name. Unaccepted formats raise an error. In that case, experiment or leave the field blank.

html = """Hello John, <br>
            I'm just testing my new fancypants email sending system here.<br>
            <b>Adam</b>"""
ourmailsender.set_message(plaintext, "This is a test", "Adam Adamson", html, "attachment.txt", "attachment.txt")

# Next, we set the recipient for our email. The recipients are always entered as a list (or tuple) even when
# there is only one recipient

ourmailsender.set_recipients(['j.doe@somewhere.com'])

# We're almost there! Now we just have to connect to the SMTP server using the account and address we specified when
# we created our MailSender, and send the email.

ourmailsender.connect()
ourmailsender.send_all()

# After all messages are sent, the connection to the server is automatically closed by default. For how to disable this,
# see the Readme.
