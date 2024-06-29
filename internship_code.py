import json
import boto3
import pyttsx3 as pt


def send_email_function(email, subject, Message):
    aws_region = 'us-east-1'
    lambda_function_name = 'sahil-python-serverless-dev-hello'
    aws_access_key_id = 'Your_access_code'
    aws_secret_access_key = 'Your_Secret_Code'

    lambda_client = boto3.client(
    'lambda',
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

    payload = {
  "email": email,
  "subject": subject,
  "message": Message
}

    try:
        response = lambda_client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',  # Can be 'Event' for asynchronous invocation
        Payload=json.dumps(payload)  # Convert payload to JSON string if needed
    )

        response_payload = response['Payload'].read().decode('utf-8')
        print(f"Lambda function response: {response_payload}")

    except Exception as e:
        print(f"Error invoking Lambda function: {str(e)}")

def main():
    engine = pt.init()
    engine.say("Enter Your Email")
    engine.runAndWait()
    email = input("Enter Your Email: ")
    
    engine.say("Enter Your Subject")
    engine.runAndWait()
    subject = input("subject for email? ")
    
    engine.say("Enter Your Message")
    engine.runAndWait()
    message = input("What do you want to say? ")
    send_email_function(email, subject, message)

main()
