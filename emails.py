import datetime as dt
import smtplib
from email.mime.text import MIMEText


def main():

    date_today = dt.datetime.now()
    send_email_stocks(False, date_today)


def send_email_stocks(update_success, date):
   s = smtplib.SMTP('smtp.gmail.com', 587)
   s.starttls()
   s.login('eastmore.notif@gmail.com', 'Eastmore123')

   sender = 'eastmore.notif@gmail.com'
   recipients = 'cdelisle@eastmoregroup.com'
   #recipients = 'dkhetsomphou@eastmoregroup.com; cdelisle@eastmoregroup.com'

   if update_success:
       msg = MIMEText('Test email {:%m/%d/%Y}.'.format(date))
       msg['Subject'] = 'Test email.'
   else:
       msg = MIMEText('Test email alert {:%m/%d/%Y}!'.format(date))
       msg['X-Priority'] = '2'
       msg['Subject'] = 'Test email.'

   msg['From'] = sender
   msg['To'] = recipients

   s.send_message(msg)
   s.quit()


if __name__=="__main__":
    main()