import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtp_host = "smtp.gmail.com"
smtp_prot = 587
from_email = 'voice.checkup@gmail.com'
to_email = 'voice.checkup@gmail.com'
username = 'voice.checkup@gmail.com'
password = 'voice12345'

msg = MIMEMultipart()
msg = message.EmailMessage()
msg.set_content('今日の結果はこちらです')
msg['subject'] = 'こんにちは'
msg['From'] = from_email
msg['To'] = from_email
msg['Bcc'] = to_email

# att1 = message.EmailMessage(open('2018-12-09.wav', 'rb').read())
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = '2018-12-09.wav;filename = "kyouno"'
# message.attach(att1)

server = smtplib.SMTP(smtp_host,smtp_prot)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.send_message(msg)
server.quit()