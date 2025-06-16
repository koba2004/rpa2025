import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail

def send_test_email():
    msg = make_mime_text(
        mail_to=gmail.account,
        subject = 'メール送信テストぉ',
        body='こんにちはやで。届いたかえ？テストテスト')
    send_gmail(msg)


def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['To'] = mail_to
    msg['From'] = gmail.account
    return msg

def send_gmail(msg):
    server = smtplib.SMTP_SSL(
        'setp.gmail.com', 445,
        context=ssl.create_default_context())
    server.set_debuglevel(0)
    server.login(gmail.account, gmail.password)
    server.send_message(msg)

if __name__ == '__main__':
    send_test_email()
    print('okやで.')