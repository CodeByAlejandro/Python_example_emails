import os
import sys
from pathlib import Path
from string import Template
import smtplib
from email.message import EmailMessage

password = os.getenv("GOOGLE_APP_PASSWORD")
if not password:
    print("Environmental variable 'GOOGLE_APP_PASSWORD' not set!")
    sys.exit(1)

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Alejandro De Groote'
email['to'] = 'alejandrodegroote@outlook.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name='Alejandro'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('CodeByAlejandro', password)
    smtp.send_message(email)
    print('Tis al chill kirl :P')
