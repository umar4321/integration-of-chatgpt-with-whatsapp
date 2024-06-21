import os


from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = 'ACa135809b40219cbbaf0d80ef1807a8e0'
auth_token = "ef26df1d5640f50517d74ed98831f551"
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    '''
    Send message to a Telegram user.

    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send

    Returns:
        - None
    '''

    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )
