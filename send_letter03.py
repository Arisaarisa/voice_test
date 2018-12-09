import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'voice_checkup.com'
receivers = ['voice_checkup.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
smtp_host = "smtp.gmail.com"
smtp_prot = 587
username = 'voice.checkup@gmail.com'
password = 'voice12345'

#创建一个带附件的实例]
message = MIMEMultipart()
message['From'] = "本教程", 'utf-8'
message['To'] = "测试", 'utf-8'
subject = 'Python SMTP 邮件测试'
message['Subject'] = 'utf-8'

#邮件正文内容
message.attach(MIMEText('这是本教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('2018-12-09.wav', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = '2018-12-09.wav; filename="2018-12-09.wav"'
message.attach(att1)

# # 构造附件2，传送当前目录下的 w3big.txt 文件
# att2 = MIMEText(open('w3big.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="w3big.txt"'
# message.attach(att2)

# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print ("邮件发送成功")
# except smtplib.SMTPException:
#     print ("Error: 无法发送邮件")