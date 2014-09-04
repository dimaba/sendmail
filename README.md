
Python Email Sender
===================

The Python email sender gives simplified acess to Python's built-in module for sending email over SMTP servers. The current version of the Python email sender supports plaintext and HTML style messages. 


Features
--------
* Simplifies Python's email libraries into one easy to use object
* Send email messages in plain text or HTML markup
* Connects to SMTP servers using TLS or SSL

Notable missing features:
* Attachments are not supported yet
* Does not support setting recipients as CC/BBC yet

Sending a simple plaintext message
----------------------------------

* Import or write a plaintext message in Python as a string variable.

```python
    plaintext = 'This is our message'
```

* Create a MailSender object. The MailSender object allows you to connect to an SMTP server by specifying the server address and port, as well as your username and password. If no server and port are specified, the MailSender defaults to using Gmail's SMTP server. The connection to the server can be made using SSL (default) or TLS (see a description of the MailSender class below). Check which type of connection your SMTP server supports. 

```python
    testmailsender = MailSender('username@server.com', 'password', ('smtp.server.com', 465), use_SSL=True)
```

* Set the plaintext message as the email's body. At this point you can also add a subject line and a 'From' name/address, although both of these can also be set individually later on. If no 'From' name is specified, the email will show the account through which you connect to the SMTP server as its sender.

```python
    testmailsender.set_message(plaintext, "This is our Subject line", 'John Doe <j.doe@somewhere.com>')
```

* Modify the email, if necessary. All parts of the email can be modified individually. See below for a list of relevant methods.

* Set the recipients for your email. You can either specify a complete list or tuple of all recipients (as in the example below) or add recipients one by one (see 'add_recipient'). Remember that this method requires a list or tuple as input, even if there is only one recipient.

```python
    testmailsender.set_recipients(['arthur@heartofgold.net', 'account2@somewhere.com'])
```

* Connect to the SMTP server you specified when creating the MailSender object.

```python
    testmailsender.connect()
```

* Send the email. This sends the same message to all listed participants. By default the connection to the SMTP server is closed once the email has been sent to all currently listed participants. If you want to send further emails without having to reconnect to the SMTP server, you can choose to disable this automatic disconnection.

```python
    testmailsender.send_all(close_connection=False)
```

Sending an HTML message
-----------------------
* Import or write both an HTML message and a plaintext message, stored in separate string variables. The plaintext message is shown in email clients which do not support HTML markup.

```python
    plaintext = 'This is our message'
    html = '<b>This</b> is our message'
```

* Create a MailSender object (see 'Sending a simple plaintext message')

* Set the plaintext and HTML messages as the email's body. Again, you can also add a subject line and a 'From' name at this point. 

```python
    testmailsender.set_message(plaintext, "This is our Subject line", 'John Doe', html)
```

* You can modifiy the HTML message individually.

```python
    testmailsender.set_html("<i>New html message</i>")
```

* Set recipients, connect to the SMTP server and send the email(s) as you would with a plaintext message.

Classes and Methods
-------------------
_class_ MailSender(in_username, in_password, in_server=("smtp.gmail.com", 587), use_SSL=False)
>	The MailSender handles creating email messages, connecting to the SMTP server and sending emails. Before doing anything else, you must create a MailSender object with the correct parameters for the SMTP server you will be using to send your emails. This means entering the appropriate username and password as well as the server address and port, and selecting the appropriate type of encryption/authorization (TLS or SSL). By default, the TLS protocol is used.<br><br>
Username and password must be passed as strings, the SMTP server should be passed as a list or tuple containing the server's address and port, and the choice between TLS and SSL is made by passing either True (for SSL) or False (for TSL, default). 

set_message(in_plaintext, in_subject="", in_from=None, in_htmltext=None)
>This method is responsible for creating the [MIME](https://docs.python.org/3.4/library/email.mime.html) message object for your email. You cannot modify individual parts of your email unless you have first created a MIME object using this method. Keep in mind that if you want to add an HTML version of your message to the email, you _must_ include an HTML message when calling this method, even if this HTML message consists of nothing more than an empty string. You can only use 'set_html' on email objects that have been created with a specified HTML part. For more detail on the the various parameters you can pass to this method, see their individual methods below.<br><br>
All parameters for this method must be passed as strings.

clear_message()
>Removes all plaintext and HTML messages included in your email, but does not destroy the MIME object itself. 'From', 'To' and 'Subject' are not cleared. To replace or remove these, you can simply use set_message to overwrite the existing MIME object.

set_subject(in_subject)
>Sets the subject of the email as it will be displayed in the recipient's email client. <br><br>
The subject must be passed as a string.

set_from(in_from)
>Sets the name of the sender as it will be displayed in the recipient's email client. This does _not_ change the displayed e-mail address of the sender.<br><br>
The 'From' name must be passed as a string. Recommended formatting is 'Firstname Lastname <address@server.com>'. Experiment with the appropriate formatting for your SMTP server. For instance, Gmail will accept 'From' fields consisting of only a name and will ignore included email addresses. By contrast, Outlook.com/Live/Hotmail will ignore the whole 'From' field if the email address specified is not identical to the address used to login to the server, and will not accept 'From' fields consisting only of a name.

set_plaintext(in_body_text)
>Sets the plain text message for the email. If the email does not include an HTML version, this plain text message will be displayed to all recipients. If the email does include an HTML versoin, this plain text message will be displayed only to recipients whose email client does not support HTML markup in emails.<br><br>
The plain text message must be passed as a string.

set_html(in_html)
> Sets the HTML message for the email. This method can only be used if you have specified an initial HTML message upon creating the message object (see 'set_message'). <br><br>
The HTML message must be passed as an HTML-formatted string. 

set_recipients(in_recipients)
> Sets the full list (or tuple) of recipients to which the email will be sent. Keep in mind that if you pass a tuple rather than a list, sending emails will work but you will nog be able to add any further recipients via 'add_recipient'. <br><br>
The participants must be passed as a list or tuple of e-mail addresses (strings). 

add_recipient(in_recipient)
> Adds one recipient to the end of the list of recipients. The list of participants is initialized as an empty list on creation of the MailSender object, so you do not need to specify your own list of participants before using 'add_recipient'.<br><br>
The recipient's email address must be passed as a string.

connect()
> Connects to the SMTP server using the username, password and authorization method specified on creation of the MailSender object.

disconnect()
> Closes the connection to the SMTP server. You must call this method if you want to close the connection to the server without having sent your email, or if you have sent your emails with the automatic disconnection disabled (see 'send_all').

send_all(close_connection = True)
> Sends the email to all specified recipients, one by one. By default, the connection to the SMTP server is automatically closed when all emails have been sent. If you do not want the connection to be automatically closed you can call 'send_all' with the parameter 'close_connection' set to False (see 'Sending a simple plain text message').


Recommended settings
--------------------
Gmail/GoogleApps:
- Using SSL: smtp.gmail.com, port 465
- Using TLS: smtp.gmail.com, port 587

Outlook.com/Live/Hotmail
- Using TLS: smtp.live.com, port 587