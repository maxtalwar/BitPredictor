import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "johnleafer05@gmail.com"  # Enter your address
passwordDefault = 'Sq1.4142'

receiver_emailDefault = "max.talwar@menloschool.org"  # Enter receiver address

messageDefault = """\
Subject: Hi there

It looks like you haven't specified an email, so a default was sent
as confirmation that your code works"""

def createMessage(subject, body):
    message = """\
    Subject: BitTrader


    Program return: %s
    """
    message = message % (str(body))
    return message




def sendEmail(message = messageDefault, password = passwordDefault, receiver_email=receiver_emailDefault):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print(email)
    print("Email sent")

"""email = createMessage("TestSubject", 3)

sendEmail(email)"""