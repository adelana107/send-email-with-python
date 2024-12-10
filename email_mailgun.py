import requests

# Use environment variables for sensitive information
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox5c63f9613d0344dca5c053f3d1715fd3.mailgun.org/messages"  # No comma
MAILGUN_API_KEY = "b7e021343f0155dc8c084703e1da98e1-da554c25-77db6d82"  # Set this in your environment variables or hardcode for testing (but don't push it publicly)

FROM_NAME = 'Unisex university'
FROM_EMAIL = 'Adelana787898@gmail.com'

TO_EMAILS = ['terryfyeargan@gmail.com']
SUBJECT = 'TESTING TESTING'
CONTENT = 'HELLO, HABIBI'

try:
    response = requests.post(
        MAILGUN_API_URL,  # Ensure this is a string, not a tuple
        auth=('api', MAILGUN_API_KEY),  # Ensure the API key is passed correctly
        data={
            'from': f'{FROM_NAME} <{FROM_EMAIL}>',
            'to': TO_EMAILS,
            'subject': SUBJECT,
            'text': CONTENT
        }
    )
    response.raise_for_status()  # Raise an error for unsuccessful status codes
    print(f"Email sent successfully! Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Failed to send email: {e}")

