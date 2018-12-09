
from email import message
# from email import Encoders
#
# import mine as mine
# from email.MIMEBase import MIMEBase


import smtplib
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


# 添付ファイルのMIMEタイプを指定する
# attachment = MIMEBase(mine['type'], mine['subtype'])
#
# file = open(f"{datetime.date.today()}.wav")
# attachment.set_payload(file.read())
# file.close()
# Encoders.encode_base64(attachment)
# msg.attach(attachment)
# attachment.add_header("Content-Dispositon", "attachment", filename=f"{datetime.date.today()}.wav")

server = smtplib.SMTP(smtp_host,smtp_prot)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.send_message(msg)
server.quit()
