import os
import sendgrid
from sendgrid.helpers.mail import Mail
import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing feedback submission...')

    try:
        req_body = req.get_json()
        name = req_body.get('name')
        email = req_body.get('email')
        message = req_body.get('message')

        sg = sendgrid.SendGridAPIClient(api_key=os.environ['SENDGRID_API_KEY'])
        content = f"Hi {name},\n\nThank you for your feedback! I am glad you test it out."

        mail = Mail(
            from_email='ibheatrix@gmail.com',
            to_emails=email,
            subject='Thanks for your feedback!',
            plain_text_content=content
        )
        sg.send(mail)

        return func.HttpResponse("Email sent successfully.", status_code=200)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("Error sending email.", status_code=500)
