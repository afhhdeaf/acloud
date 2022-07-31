import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(addr, code):
    EMAIL_FROM = 'cquptriven@qq.com'
    EMAIL_HOST_PASSWORD = 'tqixbzxlbrjgbgah'
    EMAIL_HOST, EMAIL_PORT = 'smtp.qq.com', 465
    content = '您的验证码是：{}'.format(str(code)) + '\n' + '10分钟内有效'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[请勿回复]CQUPTCloud 验证码'
    msg['From'] = '%s <%s>' % ("admin", "重邮云")
    msg['To'] = '%s <%s>' % ("client", addr)
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate()
    textplain = MIMEText('{}'.format(content), _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)
    try:
        client = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        client.login(EMAIL_FROM, EMAIL_HOST_PASSWORD)
        client.sendmail(EMAIL_FROM, [addr], msg.as_string())
        client.quit()
        return True
    except Exception as e:
        print(str(e))


def notify(content, addr):
    EMAIL_FROM = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST, EMAIL_PORT = '', 80
    replyto = EMAIL_FROM
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '[请勿回复]RivenCloud 操作通知'
    msg['From'] = '%s <%s>' % ("admin", EMAIL_FROM)
    msg['To'] = '%s <%s>' % ("client", addr)
    msg['Reply-to'] = replyto
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate()
    textplain = MIMEText('{}'.format(content), _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)
    try:
        client = smtplib.SMTP()
        client.connect(EMAIL_HOST, EMAIL_PORT)
        client.login(EMAIL_FROM, EMAIL_HOST_PASSWORD)
        client.sendmail(EMAIL_FROM, [addr], msg.as_string())
        client.quit()
        return True
    except:
        return False


if __name__ == "__main__":
    print(sendmail('1034059311@qq.com', 123456))
