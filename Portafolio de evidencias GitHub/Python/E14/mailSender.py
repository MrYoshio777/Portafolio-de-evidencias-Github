import smtplib, getpass, mimetypes, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
account = str(input('Ingresa el correo(GMAIL) con el cual lo quieres enviar: '))
password = getpass.getpass()
smtp.login(account,password)

print('Conexion exitosa con Gmail')

to = str(input('Ingresa el correo al cual lo quieres enviar: '))
subject = str(input('Con asunto: '))
cuerpo = str(input('Y cuerpo: '))

msg = MIMEMultipart()
msg['From'] = account
msg['To'] = to
msg['Subject']= subject
msg.attach(MIMEText(cuerpo))

filename = "momazo.jpg"  # In same directory as script

with open(filename, "rb") as attachment:

    part = MIMEBase("application" , "octet-stream")
    part.set_payload(attachment.read())
# Encode file in ASCII characters to send by email
encoders.encode_base64(part)
# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
# Add attachment to message and convert message to string
msg.attach(part)
text = msg.as_string()
# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(account, password)
    server.sendmail(account, to, text)
