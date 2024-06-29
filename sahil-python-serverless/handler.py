import json
from smtplib import SMTP


def hello(event, context):

    try:
        receiver_email = event.get('email')
        receiver_subject = event.get('subject')
        receiver_message = event.get('message')
        if not (receiver_email or receiver_subject or receiver_message): 
            raise ValueError("Missing required fields: email, subject, or Message")
        send_email_to_rec(receiver_email, receiver_subject, receiver_message)
        response_body = {
            'message':"successfully sent email"
        }
        return {"statusCode": 200, "body": json.dumps(response_body)}
    except Exception as e:
        error = {
        'error':str(e)
        }
        return {"statusCode": 500, "body": json.dumps(error)}


def send_email_to_rec(receiver_email, receiver_subject, receiver_message):
    server = 'smtp.gmail.com'
    port = 587
    email = "natsu21202@gmail.com"
    password = 'caxghvzugthklhaj'
    server = SMTP(server, port)
    server.starttls()

    server.login(email, password)
    message = f'Subject: {receiver_subject}\n\n{receiver_message}'
    server.sendmail(email, receiver_email, message)

