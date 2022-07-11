import smtplib, ssl, getpass

port = 465  #SSL
smtp_server = "smtp.gmail.com"

sender_email = input("Insert your e-mail address: ")  #use this for your address
password = getpass.getpass(prompt="Input password and press enter: ") #input the password tied to the e-mail account. getpass prevents it from being seen on the input field.
receiver_email = input("Insert destination address: ") #this is who the e-mail will be sent to. so far only gmail and outlook accounts are accepted.

#main loop and server connection stuff
if '@gmail.com' or '@outlook.com' in receiver_email: #there's gotta be a better way to get this working.
    subject = input("Insert subject: ")
    message = input("Input message: ")
    body = "Subject: " + subject + '\n' + message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, body)
    print('Message sent.')
else:
    print("Invalid e-mail or password.")