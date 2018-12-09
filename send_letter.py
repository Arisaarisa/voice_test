import smtplib

from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def create_message(from_addr, to_addr, subject, body, mine, attach_file):
    """
    Mailのメッセージを構築する
    """
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr


    body = MIMEText(body)
    msg.attach(body)

    #添付ファイルのMIMEタイプを指定する
    attachment = MIMEBase(mine['type'],mine['subtype'])

    file = open(attach_file['path'])
    attachment.set_payload(file.read())
    file.close()
    Encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header("Content-Dispositon","attachment",filename=attach_file['name'])

    return msg

def sendGmail(from_addr, to_addr, msg):
    """
    mailを送信する
    """
    smtp = smtplib.SMTP_SSL(host, port)
    smtp.ehlo()
    smtp.login(username, password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit()


if __name__ == '__main__':

    #gmail用に追加
    host, port = 'smtp.gmail.com', XXX
    username, password = 'hogehoge@gmail.com', 'hogehoge'

#実際に使用されているアドレスだと困るので、コメントアウトしてます。

    from_addr = #"hogehoge@gmail.com”
    to_addr = #"hogehoge@gmail.com"
    subject = "ファイル添付"
    body = "test body"
    mine={'type':'text','subtype':'comma-separated-values'}

    attach_file={'name':'test.csv','path':'/tmp/test.csv'}
    msg = create_message(from_addr, to_addr, subject, body, mine, attach_file)
    sendGmail(from_addr, to_addr, msg)