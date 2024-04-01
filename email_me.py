import smtplib
import random
import imaplib
import email

from credentials import EMAIL, SENDER_EMAIL, PASSWORD, ACTIVITIES, INTERVALS

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def check_email():
    username = EMAIL
    password = PASSWORD
    sender_email = EMAIL

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    result, data = mail.search(None, '(FROM "{}") BODY "task" UNSEEN'.format(sender_email))

    email_ids = data[0].split()

    for email_id in email_ids:
        result, data = mail.fetch(email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        body = get_body(msg).decode()
        
        if 'task' in body:
            mail.store(email_id, '+FLAGS', '\\Seen')
            main()

    mail.close()
    mail.logout()
            
def send_email(subject, body):

    sender_email = SENDER_EMAIL
    receiver_email = EMAIL
    password = PASSWORD

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(sender_email, receiver_email, message)
    server.quit()

def determine_activity():
    activities = ACTIVITIES
                    
    intervals = INTERVALS

    return f"{random.choice(activities)} for {random.choice(intervals)} minutes."

def main():
    subject = "Your task has been delivered!"
    body = determine_activity()
    send_email(subject, body)
    

if __name__ == '__main__':
    check_email()
