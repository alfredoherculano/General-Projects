from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'alfredo.hsh@gmail.com'
email_password = password

email_receiver = ''

subject = 'Testando projeto pra mandar email com o Python'
body = """
E aí cara de pica!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
	smtp.login(email_sender, email_password)
	smtp.sendmail(email_sender, email_receiver, em.as_string())