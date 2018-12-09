
from email import message
import smtplib

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'voice.checkup@gmail.com'  # 送信元のアドレス
to_email = 'voice.checkup@gmail.com'  # 送りたい先のアドレス
username = 'voice.checkup@gmail.com'  # Gmailのアドレス
password = 'voice12345'  # Gmailのパスワード

# メールの内容を作成
msg = message.EmailMessage()
msg.set_content('test mail')  # メールの本文
msg['Subject'] = 'test mail(sub)'  # 件名
msg['From'] = from_email  # メール送信元
msg['To'] = to_email  # メール送信先

# メールサーバーへアクセス
server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()